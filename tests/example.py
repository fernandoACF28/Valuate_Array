# here some example to get dataframe from netCDF file
from functions import *
window_sizes = [1, 5, 11, 25]

files_nc = gb('/home/fernando/Documents/Dark Target HDF Files/MYD04_L2_netCDF_final/2002/*.nc')
ds = xr.open_dataset(files_nc[7])

Getting_dataframe_from_hdf(ds,'AOD_550nm','time',estacoes_america_sul,window_sizes,'teste')