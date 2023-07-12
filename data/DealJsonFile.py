import json
import csv

directory = "/Users/matt/Desktop/20230705/20230707/"
dataPath = directory+"15.11-10-59.json"

output_self = directory+ "cloud_self.txt"
output_others = directory+ "cloud_otherCars.txt"

# 从文件中读取 JSON 数据
with open(dataPath, 'r') as file:
    json_str = file.read()

# 解析 JSON 字符串为 Python 对象
data = json.loads(json_str)

print(data[0]['time'])

# 访问解析后的数据
# ...

self_file_writer = csv.writer(open(output_self, 'w'))
others_file_out = open(output_others, 'w')
# 遍历键和值
for parentItem in data:
    # print(parentItem)
    time = parentItem['time']
    selfLon = 0.0
    selfLat = 0.0
    selfAlt = 0.0
    selfAngle = 0.0
    strTemp = ""
    for item in parentItem['allList']:
        # print(item)
        # if item['uuid'] == 'vehicle':
        if item['uuid'] == '1':
            selfLon = item['wgslon']
            selfLat = item['wgslat']
            selfAngle = item['heading']
        else:
            strTemp += "{},{},{},{},{},{},{},".format(item['uuid'],item['wgslon'], item['wgslat'],0.0,item['heading'],item['type'],'')
            # strTemp += "{},{},{},{},{},".format(item['type'],item['wgslon'], item['wgslat'],item['heading'],item['uuid'])

    self_file_writer.writerow([time,selfLon,selfLat,selfAlt,selfAngle])
    # print(strTemp)
    # if strTemp != '':
    others_file_out.write("{};{}\n".format(time,strTemp))


