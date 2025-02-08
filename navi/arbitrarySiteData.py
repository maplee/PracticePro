# import json
# import csv
# import os
# import sys
#
# def readFile(csv_site,csv_path):
#     with open(csv_path, 'wr', newline='') as file:
#         # 创建CSV读取器
#         csv_path_reader = csv.reader(file)
#         # 读取每一行数据
#         for row in csv_reader:
#             # 打印每一行的数据
#             print('ready',row)
#             if row[0] != '191817':
#                 continue
#
#
# if __name__ == "__main__":

import pandas as pd
import os

# 设置包含路径的CSV文件的路径
path_csv_path = '/Users/matt/Desktop/arbitrary_site_route_track_bj.csv'

# 设置包含站点数据的CSV文件的路径
data_csv_path = '/Users/matt/Desktop/arbitrary_site_bj.csv'

# 设置输出CSV文件的路径
output_csv_path = '/Users/matt/Desktop/arbitrary_site_route_track_bj_output.csv'

# 读取包含路径的CSV文件
path_df = pd.read_csv(path_csv_path,header=None)
path_df.columns=['0','1','2','3','4','5','6']

# 初始化一个空的DataFrame来存储结果
result_df = pd.DataFrame(columns=path_df.columns.tolist())

# 遍历路径文件中的每一行
for index, row in path_df.iterrows():
    path = row['3']
    print(path)
    station_ids = path.split("-")  # 提取站点ID

    # 使用站点ID从另一个CSV文件中检索站点数据
    data_df = pd.read_csv(data_csv_path,header=None)
    data_df.columns = ['0', '1', '2', '3', '4']
    station_data1 = data_df[data_df['1'] == station_ids[0].strip()]
    station_data2 = data_df[data_df['1'] == station_ids[1].strip()]

    print('starting point:',station_data1['4'].values)
    print('end point:',station_data1['4'].values)

    # 将原始路径和检索到的站点数据附加到结果DataFrame中
    result_row = row.to_dict()  # 将当前行转换为字典
    result_row['4'] = station_data1['4'].values[0] # 添加站点数据列
    result_row['6'] = station_data2['4'].values[0] # 添加站点数据列
    # result_df = result_df.append(result_row, ignore_index=True)  # 将新行附加到结果DataFrame中

    # lonlatData = {
    #     '4': station_data1['4'].values,
    #     '6': station_data2['4'].values
    # }
    # lonlat_df = pd.DataFrame(lonlatData)
    lonlat_df = pd.DataFrame([result_row])
    result_df = pd.concat([result_df,lonlat_df], ignore_index=False)  # 将新行附加到结果DataFrame中

# 将结果DataFrame保存到新的CSV文件中
result_df.to_csv(output_csv_path, index=False,header=False)

# 打印输出文件的路径以确认
print(f"Data has been saved to: {output_csv_path}")