import pandas as pd
import os
from geopy.distance import geodesic


# 设置包含站点数据的CSV文件的路径
data_csv_path = '/Users/matt/Desktop/arbitrary_site_bj_0419.csv'

# 设置输出CSV文件的路径
output_full_csv_path = '/Users/matt/Desktop/arbitrary_site_full_route_track_bj_0419.csv'

# 设置抽取20行输出CSV文件的路径
output_csv_path = '/Users/matt/Desktop/arbitrary_site_route_track_bj_0419.csv'

# 从 CSV 文件中随机抽取20行并存入新文件
def random_sample_and_save(filename=output_full_csv_path, sample_size=20, output_filename=output_csv_path):
    df = pd.read_csv(filename)
    sample = df.sample(n=sample_size)
    sample.to_csv(output_filename, index=False)



# 读取包含路径的CSV文件
data_df = pd.read_csv(data_csv_path,header=None)
data_df.columns = ['0', '1', '2', '3', '4']

paths = []
# 遍历路径文件中的每一行
for index, row in data_df.iterrows():
    station_start_name = row['1']
    station_start_lonlat = row['4']
    # 倒序遍历
    for indexEnd, rowEnd in data_df.iloc[::-1].iterrows():
        station_end_name = rowEnd['1']
        station_end_lonlat = rowEnd['4']
        station_start_lonlats = station_start_lonlat.split(",")
        station_end_lonlats = station_end_lonlat.split(",")
        distance = geodesic((station_start_lonlats[1],station_start_lonlats[0]),(station_end_lonlats[1],station_end_lonlats[0])).meters
        print(station_start_name,station_end_name,'distance:',distance)
        if distance<3000:
            continue
        path_data = {
            'id': "{}-{}".format(index,indexEnd),
            'cityId': 110000,
            'name': "{}-{}".format(station_start_name,station_end_name),
            'path': "{}-{}".format(station_start_name,station_end_name),
            'start': station_start_lonlat,
            'waypoint': '',
            'end': station_end_lonlat,
            'distance': distance
        }
        paths.append(path_data)

# 将结果DataFrame保存到新的CSV文件中
paths_df = pd.DataFrame(paths)
paths_df.to_csv(output_full_csv_path, index=False,header=False)

# 打印输出文件的路径以确认
print(f"Data has been saved to: {output_csv_path}")

random_sample_and_save(output_full_csv_path,19,output_csv_path)