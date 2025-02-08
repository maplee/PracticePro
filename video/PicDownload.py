from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import requests
import urllib.parse
from datetime import datetime

# Function to download image from URL
def download_image(index,url, directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(directory, 'img_'+str(index)+'.jpeg'), 'wb') as file:
                file.write(response.content)
                print(f"Image downloaded: {url}")
        else:
            print(f"Failed to download image: {url}")
    except Exception as e:
        print(f"Exception occurred while downloading image: {url}\n{e}")


def download_images_from_baidu_image_search(search_word, downloaded_images,max_downloads=10):
    # 设置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # 启动ChromeDriver
    # driver = webdriver.Safari(options=chrome_options)

    driver = webdriver.Chrome(options=chrome_options)

    # 构造搜索URL
    search_url = f'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&ctd=&sid=&word={search_word}'

    # 打开网页
    driver.get(search_url)

    # 等待页面加载
    time.sleep(2)
    # print(driver.page_source)

    # 创建一个目录来保存下载的图片
    os.makedirs(downloaded_images, exist_ok=True)
    # if not os.path.exists(downloaded_images):
    #     os.makedirs(downloaded_images)
    image_elements = driver.find_elements(By.TAG_NAME, 'img')
    count = 0;
    for index, image_element in enumerate(image_elements):
        image_src = image_element.get_attribute('data-imgurl')
        if not image_src:
            continue
        try:
            print("image_src:",image_src)
            if 'http' in image_src:
                download_image(index,image_src, downloaded_images)
                count += 1
            else:
                continue
        except Exception as e:
            print(f'An error occurred while downloading image {index + 1}: {e}')
            break  # 如果出现错误，停止下载
    print("下载了",count,"张图片")
    # 关闭浏览器驱动
    driver.quit()

def dealSearchFile():
    filename = '/Users/matt/Downloads/100个三四线城市.txt'
    lines = []

    marker = "**"

    with open(filename, 'r') as file:
        for line in file:
            # 找到开始和结束标记的索引
            start_index = line.find(marker) + len(marker)
            end_index = line.find(marker, start_index)

            # 截取开始和结束标记之间的文本
            content = line[start_index:end_index].strip()
            print(content)
            lines.append(content)  # 使用 strip() 移除每行的前后空白字符

    # 此时 lines 数组包含了文本文件中的每一行
    return lines


def main():
    # 要搜索的关键词
    # searchWords = ['大理','凤凰古城','川藏线','五台山','桂林','老君山','敦煌','月牙泉','西安','南昌','济南','杭州']
    searchWords = dealSearchFile()
    total_time = 0
    for word in searchWords:
        print(word)
        start_time = time.time()
        search_word = urllib.parse.unquote(word)
        # 提取并下载图片
        nowDateStr = str(datetime.now().date()).replace("-", "")
        downloaded_images = "/Users/matt/Downloads/material/"+nowDateStr+"/"+search_word+"/"
        download_images_from_baidu_image_search(search_word, downloaded_images,max_downloads=1000)  # 下载前5张图片
        end_time = time.time()
        print(word,"执行时间: ", end_time - start_time, "秒")
        total_time += end_time - start_time
    print("总耗时: ",total_time, "秒")
if __name__ == '__main__':
    main()
