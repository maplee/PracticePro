import sys

import requests
import json
import csv
import os
from datetime import datetime



def download_file(id,cityId,routeName,url, destination_folder,sucess_fwriter,fail_fwriter):
    # 发送GET请求
    print('route start:',id)
    response = requests.get(url)
    print('response status code:',response.status_code)

    if response.status_code == 200:
        responseJson = json.loads(response.content)
        # print(responseJson)
        # 使用BeautifulSoup解析HTML内容
        # soup = BeautifulSoup(response.text, 'html.parser')
        # 找到文件下载链接
        # file_link = soup.find('a', {'class': 'download-link'})  # 请替换为实际的HTML元素和属性
        code = responseJson['code']
        if code != '0':
            print("fail:",responseJson['msg'])
            print('route over:', id)
            fail_fwriter.writerow([id,cityId,routeName,url])
            return
        data = responseJson['data']
        # print('data:',data)
        file_url = data['filePath']
        csv_file_md5 = data['fileMd5']
        csv_file_name = 'traj_'+id+'.csv'
        csv_file_source_name = data['fileName']
        print('download url:',file_url)
        # 获取文件名
        name = file_url.split('/')[-1]
        # print('name:',name)
        nowDateStr = str(datetime.now().date()).replace("-", "")
        name = id + '_' + cityId + '_' + nowDateStr + '_' + routeName+".csv"
        file_name = os.path.join(destination_folder,name)
        # print('file_name:',file_name)
        txt_file_url = 'https://api.zhidaohulian.com/fileServer/upload/downloadFileStream?key=fileServer/online_car_hailing/119a1805fb6075bc165cb407cb7d3d28/stop_191850.txt'
        txt_file_md5 = '119a1805fb6075bc165cb407cb7d3d28'
        txt_file_name = 'stop_'+id+'.txt'
        txt_file_source_name = 'stop.txt'
        # line_id,brand,car_model,csv_file_url,csv_file_md5,csv_file_name,csv_file_source_name,txt_file_url,txt_file_md5,txt_file_name,txt_file_source_name
        sucess_fwriter.writerow([id,'东风','E70',file_url,csv_file_md5,csv_file_name,csv_file_source_name,txt_file_url,txt_file_md5,txt_file_name,txt_file_source_name])
        # 下载文件
        with open(file_name, 'wb') as file:
            file.write(requests.get(file_url).content)

        print(f"download success: {file_name}")

    else:
        print(f"request fail code: {response.status_code}")

    print('route over:', id)

def readFile(csv_path,download_folder):
    with open(csv_path, 'r', newline='') as file:
        # 创建CSV读取器
        csv_reader = csv.reader(file)
        outputSucessFileName = download_folder+"output_scuess.csv"
        outputFailFileName = download_folder+"output_fail.csv"
        sucess_fwriter = csv.writer(open(outputSucessFileName, "w"))
        fail_fwriter = csv.writer(open(outputFailFileName, "w"))

        sample_url = "http://route-qa.zhidaozhixing.com/route?qaFlag=0&cityId="
        # sample_url = "http://172.30.33.88:8082/route?qaFlag=0&cityId="
        sample_url = "http://127.0.0.1:8082/route?qaFlag=0&cityId="
        # 读取每一行数据
        for row in csv_reader:
            # 打印每一行的数据
            print('ready',row)
            # if row[0] != '191806':
            #     continue
            # if row[5]:
            #     target_url = "{}{}&points={},{},{}".format(sample_url, row[1], row[4], row[5], row[6])
            # else:
            target_url = "{}{}&points={},{},{},{}".format(sample_url,row[1], row[2],row[3], row[4],row[5])
            print('request url:',target_url)
            download_file(row[0],row[1],row[2],target_url, download_folder,sucess_fwriter,fail_fwriter)

if __name__ == "__main__":
    nowDateStr = str(datetime.now().date()).replace("-", "")
    # download_folder = "/Users/matt/Downloads/"+nowDateStr+"/hy1"
    # csv_path = "/Users/matt/Downloads/hy_data_new_0328.csv"
    # download_folder = "/Users/matt/Downloads/"+nowDateStr+"/bj"
    # csv_path = "/Users/matt/Downloads/bj_data_0119.csv"
    download_folder = "/Users/matt/Downloads/"+nowDateStr+"/bj"
    csv_path = "/Users/matt/Downloads/bj_test.csv"

    if len(sys.argv) != 2:
        print("批处理参数使用默认值：",csv_path,download_folder)
    else:
        csv_path = sys.argv[1]
        download_folder = sys.argv[2]
        print("批处理参数：",csv_path,download_folder)

    if not os.path.isdir(download_folder):
        os.makedirs(download_folder)

    readFile(csv_path,download_folder)
    # download_file(target_url, download_folder)
