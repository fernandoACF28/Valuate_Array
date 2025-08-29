import numpy as np
import pandas as pd
import os
import xarray as xr

def select_pixels(ds,var:str,
                  station: tuple[float, float],
                  window_size:int,lat,lon):
    ds = ds[var]
    change_lat,change_lon= lat,lon 
    lat_station,lon_station = station[0],station[1]
    lat_idx = np.abs(ds[lat].values - lat_station).argmin()
    lon_idx = np.abs(ds[lon].values - lon_station).argmin()
    lat_start = max(0, lat_idx - window_size)
    lat_end = min(len(ds[lat]), lat_idx + window_size + 1)  
    lon_start = max(0, lon_idx - window_size)
    lon_end = min(len(ds[lon]), lon_idx + window_size + 1)

    DatArray = ds.isel(change_lat=slice(lat_start, lat_end),
                    change_lon=slice(lon_start, lon_end))
    return DatArray


def get_mean_and_STD(ds_filled,var,time_index):
    """
    ds_filled -->> data spatial filtered around the station.
    var -->> name of var of interesting
    time_index -->> it's important, because you have diferents arrays in time,
    you need to specify the index of time.
    """
    val_mean = ds_filled[var].isel(time=time_index).mean().values.item()
    std_val = ds_filled[var].isel(time=time_index).std().values.item()
    return val_mean,std_val

def valid_windows(number):
    """
    number --->> win_size
    if my window size is equal to 1, i need to check the pixels around
    the station, for that, its only add plus 2 and take square, after that i have 
    the number of values in matrix (win_size+2)**2 = 9 pixels with center value.
    But we need only half of samples avaible, for that, we take minus one pixel (central_value) and divided by/2.
    """
    number += 2  
    return int((number**2-1)/2)




def Getting_dataframe_from_netCDF(ds_oppened,
                               var_ds: str,
                               coordinate_time: str,
                               dict_stations: dict,
                               window_sizes: list[int],
                               path_out: str,
                               lat='lat',
                               lon='lon'):
    ds = ds_oppened
    data_list = []
    size_time = len(ds[var_ds][coordinate_time])
    
    for station in dict_stations:
        coords_station, station_name = dict_stations[station], station
        
        for i_time in range(size_time):
            dictionary_station = {
                'station': station_name,
                f'{coordinate_time}': ds[f'{coordinate_time}'].values[i_time]
            }
            
            sequence_broken = False 
            for win in sorted(window_sizes): 
                
                if sequence_broken:
                    dictionary_station[f'mean_px_{win}x{win}'] = np.nan
                    dictionary_station[f'std_px_{win}x{win}'] = np.nan
                    continue
                
                ds_filled = select_pixels(ds=ds, var=[var_ds],
                                          station=coords_station,
                                          window_size=win,
                                          lat=lat,
                                          lon=lon)
                
                arr = ds_filled[var_ds].isel(time=i_time).values
                valid_pixels = int(np.sum(~np.isnan(arr)))
                valid_win = valid_windows(win)
                
                if isinstance(valid_win, int) and valid_pixels >= valid_win:
                    val_mean, val_std = get_mean_and_STD(ds_filled, var_ds, i_time)
                    dictionary_station[f'mean_px_{win}x{win}'] = val_mean
                    dictionary_station[f'std_px_{win}x{win}'] = val_std
                else:
                    dictionary_station[f'mean_px_{win}x{win}'] = np.nan
                    dictionary_station[f'std_px_{win}x{win}'] = np.nan
                    sequence_broken = True 
            data_list.append(dictionary_station)
    
    df = pd.DataFrame(data_list)
    os.makedirs('Parquet_datas', exist_ok=True)
    df.to_parquet(f'Parquet_datas/{path_out}.parquet', index=False)

    
def Getting_dataframe_from_hdf(hdf_open,
                               var_ds: str,
                               coordinate_time: str,
                               dict_stations: dict,
                               window_sizes: list[int],
                               path_out: str):
    ds = hdf_open
    data_list = []
    try:
        size_time = len(ds[var_ds][coordinate_time])
    except: 
        print('Your hDF file need a time coordinate!')

    for station in dict_stations:
        coords_station, station_name = dict_stations[station], station
        
        for i_time in range(size_time):
            dictionary_station = {
                'station': station_name,
                f'{coordinate_time}': ds[f'{coordinate_time}'].values[i_time]
            }
            
            sequence_broken = False 
            for win in sorted(window_sizes): 
                
                if sequence_broken:
                    dictionary_station[f'mean_px_{win}x{win}'] = np.nan
                    dictionary_station[f'std_px_{win}x{win}'] = np.nan
                    continue
                
                ds_filled = select_pixels(ds=ds, var=[var_ds],
                                          station=coords_station, window_size=win)
                
                arr = ds_filled[var_ds].isel(time=i_time).values
                valid_pixels = int(np.sum(~np.isnan(arr)))
                valid_win = valid_windows(win)
                
                if isinstance(valid_win, int) and valid_pixels >= valid_win:
                    val_mean, val_std = get_mean_and_STD(ds_filled, var_ds, i_time)
                    dictionary_station[f'mean_px_{win}x{win}'] = val_mean
                    dictionary_station[f'std_px_{win}x{win}'] = val_std
                else:
                    dictionary_station[f'mean_px_{win}x{win}'] = np.nan
                    dictionary_station[f'std_px_{win}x{win}'] = np.nan
                    sequence_broken = True 
            data_list.append(dictionary_station)
    
    df = pd.DataFrame(data_list)
    os.makedirs('Parquet_datas', exist_ok=True)
    df.to_parquet(f'Parquet_datas/{path_out}.parquet', index=False)