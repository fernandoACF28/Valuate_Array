# here some example to get dataframe from netCDF file
from functions import *
window_sizes = [1, 5, 11, 25]

stations_Aero_SA = {
'ARM_Manacapuru': (-3.212972, -60.598056),
 'ATTO-Campina': (-2.181583, -59.021861),
 'Abracos_Hill': (-10.76, -62.358333),
 'Alta_Floresta': (-9.871339, -56.104453),
 'Alta_Floresta_IF': (-9.908354, -56.064393),
 'Amazon_ATTO_Tower': (-2.144117, -58.999867),
 'Arica': (-18.471667, -70.313333),
 'Bahia_Blanca': (-39.148333, -61.721667),
 'Belterra': (-2.648483, -54.95165),
 'Brasilia_SONDA': (-15.60129, -47.71348),
 'CASLEO': (-31.798815, -69.295685),
 'CEILAP-BA': (-34.555425, -58.506411),
 'CEILAP-Bariloche': (-41.146944, -71.163333),
 'CEILAP-Comodoro': (-45.792153, -67.462875),
 'CEILAP-Neuquen': (-38.95222, -68.13666),
 'CEILAP-RG': (-51.600503, -69.31925),
 'CUIABA-MIRANDA': (-15.73091, -56.07086),
 'Cachoeira_Paulista': (-22.689, -45.006),
 'Campo_Grande_SONDA': (-20.438617, -54.538742),
 'Campus_USACH': (-33.4499, -70.681567),
 'Cordoba-CETT': (-31.524075, -64.463682),
 'El_Alto-Altiplano': (-16.509972, -68.198583),
 'Huancayo-IGP': (-12.0402, -75.3209),
 'Itajuba': (-22.41325, -45.452389),
 'Ji_Parana_SE': (-10.93425, -61.851517),
 'Ji_Parana_UNIR': (-10.882212, -61.9686),
 'La_Paz': (-16.539, -68.066467),
 'Manaus_EMBRAPA': (-2.890528, -59.969778),
 'Medellin': (6.260672, -75.577914),
 'Montevideo_FING': (-34.918167, -56.166767),
 'Mount_Chacaltaya': (-16.350139, -68.1315),
 'Natal': (-5.8415, -35.1995),
 'PSDA_Chile': (-24.090306, -69.929028),
 'Paranal_basecamp': (-24.640915, -70.387045),
 'Petrolina_SONDA': (-9.0691, -40.320108),
 'Pilar_Cordoba': (-31.667411, -63.882597),
 'Punta_Arenas_UMAG': (-53.1354, -70.8845),
 'Quito_USFQ': (-0.196244, -78.435589),
 'RdP-EsNM': (-34.818, -57.8959),
 'Rio_Branco': (-9.957467, -67.86935),
 'SANTA_CRUZ': (-17.802133, -63.177717),
 'SANTA_CRUZ_UTEPSA': (-17.767325, -63.200961),
 'SP-EACH': (-23.48163, -46.49967),
 'San_Cristobal_USFQ': (-0.8954, -89.60879),
 'Santiago_Beauchef': (-33.457222, -70.661666),
 'Sao_Martinho_SONDA': (-29.443333, -53.823444),
 'Sao_Paulo': (-23.5615, -46.734983),
 'Temuco-UFRO_CEFOP': (-38.745803, -72.615525),
 'Trelew': (-43.249806, -65.308611),
 'Tucuman': (-26.787153, -65.206697),
 'UdeConcepcion-CEFOP': (-36.84278, -73.02531)
 }



files_nc = gb('/home/fernando/Documents/Dark Target HDF Files/MYD04_L2_netCDF_final/2002/*.nc')
ds = xr.open_dataset(files_nc[7])

Getting_dataframe_from_hdf(ds,'AOD_550nm','time',estacoes_america_sul,window_sizes,'teste')
