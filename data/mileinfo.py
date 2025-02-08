

from math import radians, cos, sin, asin, sqrt
import re
import os


def haversine(lon1, lat1, lon2, lat2):
    """
    计算两个经纬度之间的球面距离。
    参数:
    lon1, lat1 -- 第一个点的经度和纬度
    lon2, lat2 -- 第二个点的经度和纬度
    返回值:
    distance -- 两点之间的距离（单位：公里）
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = abs(lon2 - lon1)
    dlat = abs(lat2 - lat1)
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))

    # 地球平均半径，单位为公里
    r = 6378.137

    return c * r

def calculate_distance(x1, y1, x2, y2):
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)*100000
    return distance

# 读取文件并计算每一行的距离和
def calculate_distance_sum(file_path):
    total_distance_autopilot = 0.0
    total_distance_other = 0.0
    count = 0

    with open(file_path, 'r') as file:
        # 使用列表推导式读取每一行，并使用分隔符分割字符串，然后存储到列表中
        data_list = [line.strip().split(",") for line in file]

    for index,data in enumerate(data_list):
        if index+1 < len(data_list):
            lon1, lat1 = map(float, [data[1], data[2]])
            lon2, lat2 = map(float, [data_list[index+1][1], data_list[index+1][2]])
            distance = haversine(lon1, lat1, lon2, lat2)
            count+=1
            # if distance*1000>10:
            #     print(count,distance*1000)
            if data_list[index+1][0] == '1':
                total_distance_other += distance
            else:
                total_distance_autopilot += distance
    print("自动驾驶里程：",total_distance_autopilot,"人工驾驶里程：",total_distance_other,count)
    return total_distance_other+total_distance_autopilot

def calculate_total_distance(file_path):
    total_distance = 0.0
    previous_lon, previous_lat = None, None

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 3:
                lon, lat = float(parts[1]), float(parts[2])
                if previous_lon is not None and previous_lat is not None:
                    total_distance += haversine(previous_lon, previous_lat, lon, lat)
                previous_lon, previous_lat = lon, lat

    return total_distance

def extract_lines_with_marker_stream(log_file_path, marker, output_file_path):
    with open(log_file_path, 'r') as file:
        with open(output_file_path, 'w') as output:
            for line in file:
                if marker in line:
                    output.write(line)

def extract_lines_with_marker_stream_del(log_file_path, output_file_path):
    pattern = r'\d+,\d+,\d+'
    with open(log_file_path, 'r') as file:
        with open(output_file_path, 'w') as output:
            for line in file:
                # 使用re.search查找匹配项
                match = re.search(pattern, line)
                # 如果找到匹配项，则输出
                if match:
                    extracted_data = match.group()
                    sp_data = extracted_data.split(',')
                    if sp_data[0] == '255':
                        continue
                    if sp_data[1] == '4294967295':
                        continue
                    lon,lat = map(float,[sp_data[1],sp_data[2]])
                    # print("Extracted Data:", extracted_data)
                    # output.write(extracted_data+'\n')
                    output.write(sp_data[0]+','+str(lon/10000000.0)+','+str(lat/10000000.0)+'\n')

# 调用函数
log_file_path = '/Users/matt/Downloads/node_custom_0923.log'
# log_file_path = 'node_custom.log'
marker='mileinfo'
logName = os.path.basename(log_file_path)
output_file_path = '/Users/matt/Downloads/miles_'+logName
output_file_path = 'miles_'+logName
extract_lines_with_marker_stream(log_file_path, marker, output_file_path)

marker_takeover='-----  takeover : '
output_file_takeover_path = '/Users/matt/Downloads/takeover_'+logName
output_file_takeover_path = 'takeover_'+logName
extract_lines_with_marker_stream(log_file_path, marker_takeover, output_file_takeover_path)


data_path = 'miles_all_'+logName
extract_lines_with_marker_stream_del(output_file_path,data_path)


distance_sum = calculate_distance_sum(data_path)
print(f"The {logName} total distance is {distance_sum} kilometers.")

# distance_sum = calculate_total_distance(data_path)
# print(f"The {logName} total distance2 is {distance_sum} kilometers.")

