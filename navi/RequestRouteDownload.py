import requests
from bs4 import BeautifulSoup
import os
import json
import csv


def download_file(id,url, destination_folder):
    # 发送GET请求
    response = requests.get(url)
    print('response status code:',response.status_code)

    if response.status_code == 200:
        responseJson = json.loads(response.content)
        print(responseJson)
        # 使用BeautifulSoup解析HTML内容
        # soup = BeautifulSoup(response.text, 'html.parser')
        # 找到文件下载链接
        # file_link = soup.find('a', {'class': 'download-link'})  # 请替换为实际的HTML元素和属性

        data = responseJson['data']
        # print('data:',data)
        file_url = data['filePath']
        print('file_url:',file_url)
        # 获取文件名
        name = file_url.split('/')[-1]
        print('name:',name)
        name = id+'_HY_'+name
        file_name = os.path.join(destination_folder,name)
        print('file_name:',file_name)
        # 下载文件
        with open(file_name, 'wb') as file:
            file.write(requests.get(file_url).content)

        print(f"文件已下载到 {file_name}")

    else:
        print(f"请求失败，状态码: {response.status_code}")

def readFile(csv_path,download_folder):
    with open(csv_path, 'r', newline='') as file:
        # 创建CSV读取器
        csv_reader = csv.reader(file)

        # 读取每一行数据
        for row in csv_reader:
            # 打印每一行的数据
            print(row)
            # if row[0] == '191636':
            #     continue
            sample_url = "http://route-qa.zhidaozhixing.com/route?qaFlag=0&cityId=430400&points"
            if row[4]:
                target_url = "{}={},{},{}".format(sample_url, row[3], row[4], row[5])
            else:
                target_url = "{}={},{}".format(sample_url, row[3],row[5])
            print(target_url)
            download_file(row[0],target_url, download_folder)

if __name__ == "__main__":
    # 替换为实际的目标URL和下载文件夹路径
    # target_url = "http://route-qa.zhidaozhixing.com/route?qaFlag=0&cityId=430400&points=112.612211,26.725855,112.577629,26.8202629"
    download_folder = "/Users/matt/Downloads/20231211/"
    csv_path = "/Users/matt/Downloads/hy_data1.csv"
    readFile(csv_path,download_folder)
    # download_file(target_url, download_folder)
