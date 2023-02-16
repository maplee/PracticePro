import requests
import prettytable as pt
from selenium import webdriver

# f = open('city.json', encoding='utf-8')
# txt = f.read()
# json_data = json.loads(txt)
# fromCity = input('请输入你要出发的城市：')
# toCity = input('请输入你要到达的城市：')
# date = input('请输入你要出发的日期（格式：2022-05-22  ）：')
# print(json_data[fromCity])
# print(json_data[toCity])
#
# url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={json_data[fromCity]}&leftTicketDTO.to_station={json_data[toCity]}&purpose_codes=ADULT'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
#     ,
#     'Cookie': '_uab_collina=165365799402790432505038; JSESSIONID=359F91290F98BC4FA6A1FB1CEF1BE77F; BIGipServerpool_passport=65274378.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1653959294875; RAIL_DEVICEID=Fx_jBGrUaMnlBi6oODpgsB8OwtdZSqRGeKv6ajeZ_lYQKLLU_y3kV5ni1aldKG6IkTyGmYkZTVmVyw-XEfAMD7J0D2xDXB2TdPGcfFsbkSeC76MRPhGYj6g-AvlL1KmBbbcrsMbYHDf_FUlq9GTShDG3TqMDVm8g; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_toDate=2022-05-27; _jc_save_wfdc_flag=dc; BIGipServerotn=2280128778.50210.0000; _jc_save_fromDate=2022-05-28}'}
# response = requests.get(url=url, headers=headers)
# print(response.json())
#
# tb = pt.PrettyTable()
#
# tb.title = '结果如下'
# tb.field_names = [
#     '序号', '车次', '发车时间', '到达时间', '耗时', '特等座', '一等座', '二等座', '软卧', '硬卧', '硬座', '无座'
# ]
# page = 0
# for lineStr in response.json()['data']['result']:
#     index = 0
#     info = lineStr.split('|')
#     num = info[3]
#     start_time = info[8]
#     end_time = info[9]
#     cost = info[10]
#     soft_sleeper = info[23]
#     hard_sleeper = info[28]
#     hard_seat = info[29]
#     privilege_seat = info[32]
#     First_class_seat = info[31]
#     second_class = info[30]
#     No_seat = info[26]
#
#     tb.add_row([
#         page, num, start_time, end_time, cost, privilege_seat, First_class_seat, second_class, soft_sleeper,
#         hard_sleeper,
#         hard_seat, No_seat])
#     page += 1
#
#     # for cStr in info:
#     #     print(index, cStr, sep='|')
#     #     index += 1
# print(tb)
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
# 绕过selenium检测
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": '''
  Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }
window.navigator.chrome = { runtime: {},  }; }
Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }
Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }
  '''
})
accout = ''
pwd = 'l1o0v8eEE'
driver.find_element(by=By.ID, value='J-userName').send_keys(accout)
driver.find_element(by=By.ID, value='J-password').send_keys(pwd)
driver.find_element(by=By.ID, value='J-login').click()
