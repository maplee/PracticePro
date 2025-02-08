import requests
import json
from datetime import datetime
import os
import re
from bs4 import BeautifulSoup



url ='https://mp.weixin.qq.com/s?__biz=MzIwODg4Mzc5OA==&mid=2247521409&idx=3&sn=86c0eb36fd56130fac63d28c4f443dcb&chksm=977e8db8a00904ae2562f90dc5ac4ca52cbf41c1dbcb73df7842dfff82d0f19c0d34e723a295&scene=27'

response = requests.get(url)
# print(response.content)
soup = BeautifulSoup(response.content, 'html.parser')

file_path_new = '/Users/matt/Downloads/学英语的100首英文歌.txt'
file_out = open(file_path_new, 'wb')

qqlist = soup.findAll('qqmusic')
for tag in qqlist:
    music_name = tag.get('music_name')
    # music_name = music_name.replace('\xc2\xa0',' ')
    music_name = music_name+"\n"
    file_out.write(music_name.encode('utf-8'))
    print(music_name)

file_out.close()
