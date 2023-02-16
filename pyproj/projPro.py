from pyproj import Transformer, CRS

# 参数1：坐标系WKID 衡阳市 WGS_1984_UTM_Zone_49N 对应 32649
# 参数2：WGS84地理坐标系统 对应 4326
transformer = Transformer.from_crs("epsg:32649", "epsg:4326")

x = 766544.7801555358
y = 2517564.4969607797
lat, lon = transformer.transform(x, y)
print("x:", x, "y:", y)
print("lat:", lat, "lon:", lon)

transformer1 = Transformer.from_crs("epsg:4326", "epsg:32649")
lat = 26.828281
lon = 112.576230

lat = 26.820373619
lon = 112.571411217

lat = 26.8297119642
lon = 112.5999756362
# 112.576230,26.828281
x, y = transformer1.transform(lat, lon)
print("1:x:", x, "y:", y, "lat:", lat, "lon:", lon)
lat, lon = transformer.transform(x, y)
print("2:x:", x, "y:", y, "lat:", lat, "lon:", lon)

lat = 26.823120117
lon = 112.574157715

lat = 26.8297141614
lon = 112.5999778334
# 112.576230,26.828281
x, y = transformer1.transform(lat, lon)
print("1:x:", x, "y:", y, "lat:", lat, "lon:", lon)
lat, lon = transformer.transform(x, y)
print("2:x:", x, "y:", y, "lat:", lat, "lon:", lon)


# crs_CGCS2000 =CRS.from_epsg(4479)    #meter#
crs_CGCS2000=CRS.from_epsg(4490)
# crs_CGCS2000=CRS.from_epsg(4528)
# crs_CGCS2000 = CRS.from_wkt(
#     'PROJCS["CGCS_2000_3_Degree_GK_CM_114E",GEOGCS["GCS_China_Geodetic_Coordinate_System_2000",DATUM["D_China_2000",
#     SPHEROID["CGCS2000", 6378137.0, 298.257222101]],
#     PRIMEM["Greenwich", 0.0],
#     UNIT["Degree", 0.0174532925199433]],
#     PROJECTION["Gauss_Kruger"],
#     PARAMETER["False_Easting",500000.0],
#     PARAMETER["False_Northing",0.0],
#     PARAMETER["Central_Meridian",114.0],
#     PARAMETER["Scale_Factor",1.0],
#     PARAMETER["Latitude_Of_Origin",0.0],
#     UNIT["Meter",1.0]]')
crs_CGCS2000 = CRS.from_wkt('PROJCS["CGCS2000_3_Degree_GK_Zone_40",GEOGCS["GCS_China_Geodetic_Coordinate_System_2000",DATUM["D_China_2000",'
                                'SPHEROID["CGCS2000",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],'
                                'PROJECTION["Gauss_Kruger"],PARAMETER["False_Easting",40500000.0],PARAMETER["False_Northing",0.0],'
                                'PARAMETER["Central_Meridian",120.0],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0],'
                                'AUTHORITY["EPSG",4528]]')
crs_WGS84 = CRS.from_epsg(4326)
from_crs = crs_WGS84
to_crs = crs_CGCS2000
transformer3 = Transformer.from_crs(from_crs, to_crs)
x, y = transformer3.transform(lon,lat)
print("5:crs_WGS84-->crs_CGCS2000:x:", x, "y:", y, "lat:", lat, "lon:", lon)
# 即为转换后的坐标，也可以分别使⽤
