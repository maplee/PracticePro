import json
import csv

directory = "/Users/matt/Downloads/"
dataPath = directory+"TraceLOG_com.mogo.launcher.f-adasGnssInfo_2023-0828-11-10-02.txt"
dataPath = directory+"TraceLOG_com.mogo.launcher.f-adasGnssInfo_2023-0906-15-46-54.txt"

output_self = directory + "cloud_self_2023-0906-15-46-54.txt"

self_file_writer = csv.writer(open(output_self, 'w'))
# 从文件中读取 JSON 数据
with open(dataPath, 'r') as file:
    for line in file:
        # 解析 JSON 字符串为 Python 对象
        data = json.loads(line)
        print(data['localTime'])
        time = data['localTime']
        item = data['msg']['GnssInfo']
        print(item);
        if 'longitude' in item:
            selfLon = item['longitude']
            selfLat = item['latitude']
            selfAlt = item['altitude']
            selfAngle = item['heading']
            satelliteTime = int(item['satelliteTime']*1000.0)
            self_file_writer.writerow([time,selfLon,selfLat,selfAlt,selfAngle,satelliteTime])





# 访问解析后的数据


