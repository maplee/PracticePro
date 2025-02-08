import requests
import json
from datetime import datetime
import os
import re
from bs4 import BeautifulSoup


header_data = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Content-Length':'48',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With':'XMLHttpRequest'
}

# 目标网页URL
search_url = "http://www.xm95522.com/mp3/"

def downloadSong(songName,download_folder):
    # 表单数据
    form_data = {
        'input': songName,
        'filter': 'name',
        'type': 'netease',
        'page': '1'
    }
    # 发送HTTP post请求
    response = requests.post(search_url, data=form_data,headers=header_data)

    flag = False

    # 确保请求成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        responseJson = json.loads(response.content)
        list = responseJson['data']
        # print(songName,len(list))

        for data in list:
            song_url = data['url']
            title = data['title']
            title = re.sub(r'\([^)]*\)', '', title)
            lrc = data['lrc']
            song_file_name = download_folder + title+'.mp3'
            lrc_file_name = download_folder + title+'.lrc'
            songResponse = requests.get(song_url)
            # 检查响应内容是否包含特定的错误信息
            error_message = '很抱歉，你要查找的网页找不到'.encode('utf-8')  # 错误信息转换为字节序列
            if error_message in songResponse.content:
                print(title,'try again!')
                continue
            else:
                try:
                    with open(song_file_name, 'wb') as file:
                        file.write(requests.get(song_url).content)
                    with open(lrc_file_name, 'wb') as file:
                        file.write(lrc.encode('utf-8'))
                    print(title, song_url)
                    flag = True
                    break
                except Exception as e:
                    print(title, 'try again!')
                    continue

    else:
        print(songName,'fail!')

    if flag:
        return 1
    else:
        return 0


def dealContent():
    # 指定文件路径
    file_path = '/Users/matt/Downloads/非常好听的50首顶级英文歌曲.txt'
    file_path_new = '/Users/matt/Downloads/非常好听的50首顶级英文歌曲_1.txt'
    file_out = open(file_path_new,'w',encoding='utf-8')
    # 使用'with'语句打开文件，这是推荐的做法，因为它可以自动关闭文件
    index = 1
    with open(file_path, 'r', encoding='utf-8') as file:  # 指定编码为'utf-8'，以避免编码错误
        # 使用for循环按行迭代文件内容
        for line in file:
            flag = '{}.'.format(index)
            if line.startswith(flag):
                file_out.write(line.replace(flag,''))
                index +=1
    file_out.close()

if __name__ == "__main__":

    # dealContent()


    fileName = 'Adele'

    nowDateStr = str(datetime.now().date()).replace("-", "")
    download_folder = "/Users/matt/Documents/songs/"+fileName+"/"

    # 指定文件路径
    file_path = '/Users/matt/Documents/songs/'+fileName+'.txt'

    if not os.path.isdir(download_folder):
        os.makedirs(download_folder)
    # 使用'with'语句打开文件，这是推荐的做法，因为它可以自动关闭文件
    count = 0
    successCount = 0
    jumpIndex = 0
    with open(file_path, 'r', encoding='utf-8') as file:  # 指定编码为'utf-8'，以避免编码错误
        # 使用for循环按行迭代文件内容
        for line in file:
            # 处理每一行
            jumpIndex +=1
            # if jumpIndex > 38:
            #     continue
            if len(line.strip())>0:
                count += 1
                title = line.strip().replace('*','')
                # if title.__contains__('-'):
                #     title = title[title.find("-")+1:]
                successCount += downloadSong(title,download_folder)


    print(file_path,'总共',count,'首','成功',successCount,'首')
