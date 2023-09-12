
import json
import math
import csv

directory = "/Users/matt/Downloads/"
dataPath = directory+"4-航拍-停车.json"

output_file = directory+ "4-航拍-停车_f.json"

# 从文件中读取 JSON 数据
with open(dataPath, 'r') as file:
    json_str = file.read()

# 解析 JSON 字符串为 Python 对象
data = json.loads(json_str)

print(data[0]['time'])

# 访问解析后的数据
# ...
def convert_angle(angle, lat):
    angle_origin = 450 - angle
    radian_origin = math.radians(angle_origin)
    radian_lat = math.radians(lat)
    radian_deal = math.atan2(math.tan(radian_origin) * math.cos(radian_lat), 1.0)
    ruler = 270 if 0 <= angle < 180 else 90
    result = ruler - math.degrees(radian_deal)
    return result

def calculate_bearing(lat1, lon1, lat2, lon2):
    # 将经纬度从度数转换为弧度
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # 计算经度差
    delta_lon = lon2 - lon1

    # 计算方向角（角度）
    y = math.sin(delta_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    bearing = math.atan2(y, x)

    # 将方向角从弧度转换为度数
    bearing = math.degrees(bearing)

    # 保证方向角在0到360度之间
    bearing = (bearing + 360) % 360.0

    bearing = convert_angle(bearing,lat1)
    return bearing

output_file_writer = open(output_file, 'w')

selfLon = 0.0
selfLat = 0.0
preSelfLon = 0.0
preSelfLat = 0.0
selfAngle = 0.0
index = 0
# 遍历键和值
for parentItem in data:

    preSelfLon = selfLon
    preSelfLat = selfLat

    # print(parentItem)
    time = parentItem['time']
    for item in parentItem['allList']:
        if item['uuid'] == '1':
            selfLon = float(item['wgslon'])
            selfLat = float(item['wgslat'])
            # selfAngle = item['heading']
            if(index >= 1):
                if(time<=1694411982000):
                    selfAngle = calculate_bearing(preSelfLat,preSelfLon,selfLat,selfLon)
                else:
                    selfAngle = calculate_bearing(selfLat,selfLon,preSelfLat,preSelfLon)

                item['heading'] = selfAngle
            break
    index += 1

output_file_writer.write(json.dumps(data))


