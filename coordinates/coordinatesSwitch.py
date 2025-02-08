from pyproj import Proj, transform

def utm_to_latlon(easting, northing, zone_number, zone_letter):
    utm_proj = Proj(proj='utm', zone=zone_number, ellps='WGS84', south=False, north=True, errcheck=True)
    lon, lat = utm_proj(easting, northing, inverse=True)
    return lat, lon

def latlon_to_utm(lat, lon):
    zone_number = utm_zone(lat, lon)
    utm_proj = Proj(proj='utm', zone=zone_number, ellps='WGS84', south=False, north=True, errcheck=True)
    easting, northing = utm_proj(lon, lat)
    return easting, northing

def utm_zone(lat, lon):
    if -80 <= lat < 84:
        zone_number = int((lon + 180) // 6) + 1
        # zone_letter = 'CDEFGHJKLMNPQRSTUVWX'[int((lat + 80) // 8)]
        return zone_number
    else:
        raise ValueError('Latitude out of UTM range')

# 示例 um:655988.28.2971268.28)
easting = 655988.28
northing = 2971268.28
zone_number = 49
zone_letter = 'N'

# UTM转换为经度和纬度
lat, lon = utm_to_latlon(easting, northing, zone_number, zone_letter)
print("经纬度：", lon,lat)

# 经度和纬度转换为UTM
easting_new, northing_new = latlon_to_utm(lat, lon)
print("新的UTM东坐标：", easting_new)
print("新的UTM北坐标：", northing_new)
