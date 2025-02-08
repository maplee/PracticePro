import csv
import re
import pandas as pd

# 原始数据
log_file_path = "/Users/matt/Downloads/卡顿问题/log1107_4.txt"
logfile = open(log_file_path, 'r')
# 将数据按行分割
lines = logfile.readlines()
# data = """
# MapEngine::render-start
# 2024-11-05 14:39:44.722 29987-30245 renderop--_PainterMgr::addHdMap--onAddDataStart-skybox--over:11
# 2024-11-05 14:39:44.722 29987-30245 renderop--_PainterMgr::addHdMap--onAddDataStart-Plane--over:17
# 2024-11-05 14:39:44.722 29987-30245 renderop--_PainterMgr::addHdMap--onAddDataStart-Weather--over:9
# 2024-11-05 14:39:44.722 29987-30245 renderop--_PainterMgr::addHdMap--onAddDataStart-StreetLight--over:8
# MapEngine::render-over
# MapEngine::render-start
# 2024-11-05 14:39:44.722 29987-30245 renderop--_PainterMgr::addHdMap--onAddDataStart-skybox--over:11
# 2024-11-05 14:39:44.722 29987-30245 renderop--_PainterMgr::addHdMap--onAddDataStart-Plane--over:17
# 2024-11-05 14:39:44.722 29987-30245 renderop--_PainterMgr::addHdMap--onAddDataStart-Weather--over:9
# 2024-11-05 14:39:44.722 29987-30245 renderop--_PainterMgr::addHdMap--onAddDataStart-StreetLight--over:8
# MapEngine::render-over
# """

# 将数据按行分割
# lines = data.strip().split('\n')

# 准备CSV文件的标题行
csv_headers = []

# 准备写入CSV的数据列表
csv_data = []

# 标记是否是数据行
is_data_line = True

o_file = '../output1.csv'
csvfile = open(o_file, 'w')
writer = csv.writer(csvfile)
isHead=True
with open(log_file_path, 'r') as file:
    for line in file:
        if line.__contains__('MapEngine::render-start'):
            is_data_line = True
        if line.__contains__('MapEngine-ttop-render--over'):
            is_data_line = False

        # if is_data_line == False:
        #     if isHead:
        #         print('head:', csv_headers)
        #         writer.writerow(csv_headers)
        #     writer.writerow(csv_data)
        #     csv_data = []
        #     isHead = False
        # 使用正则表达式提取数据
        match = re.match(r'.+?ttop-(.+?)--over:(\d+)', line)
        if match:
            title, value = match.groups()

            if is_data_line:
                if isHead:
                    csv_headers.append(title.replace('-', '_').replace(':', '_').replace('_PainterMgr','PainterMgr'))

                csv_data.append(int(value))

            else:
                if isHead:
                    csv_headers.append('render')
                    print('head:',csv_headers)
                    writer.writerow(csv_headers)
                if len(csv_data) > 70:
                    writer.writerow(csv_data)
                csv_data = []
                isHead = False
        # else:
            # print(line)

print("CSV文件已生成。")

csvReader = csv.reader(csvfile)

graphfile = open('../graph1.csv', 'w')
graphWriter = csv.writer(graphfile)

# 逐行读取CSV文件
try:
    df = pd.read_csv(o_file, encoding='utf-8')
    # 显示DataFrame的前几行，以查看表头和数据
    # 使用itertuples遍历DataFrame中的每一行
    # print(df.head())
    for row in df.itertuples(index=True):

        # if row.Index > 10:
        #     break
        # 访问行数据
        ready = row.ready
        loadDataHD_ready = row[1]
        onAddDataStart_skybox = row.onAddDataStart_skybox
        # loadDataHD

        loadDataHD = row.onAddDataStart_skybox
        + row.onAddDataStart_Plane
        + row.onAddDataStart_Weather
        + row.onAddDataStart_StreetLight
        + row.onAddDataStart_Style
        + row.onAddDataStart_guideline
        + row.onAddDataStart_lightwave
        + row.onAddDataStart_ice
        + row.onAddDataStart_water
        + row.onAddDataStart_SignalLine
        + row.onAddDataStart
        # + row.HDPanel__addHdMap__pMesh_vp
        # + row.visible_Filter
        # + row.cacheCurrent
        # + row.HDPanel__addHdMap
        + row.addHdMap
        + row.onAABBchanged_skybox
        + row.onAABBchanged_Plane
        + row.onAABBchanged_Weather
        + row.onAABBchanged_StreetLight
        + row.onAABBchanged_Style
        + row.onAABBchanged_guideline
        + row.onAABBchanged_lightwave
        + row.onAABBchanged_ice
        + row.onAABBchanged_water
        + row.onAABBchanged_SignalLine
        + row.onAABBchanged
        + row.PainterMgr__addHdMap
        opengl =  row.loadDataHD - loadDataHD

        total = row.ready + row.loadDataHD + row.renderHD + row.render

        # 打印每一行的数据
        print(f'{row.Index},total: {total}, opengl: {opengl}, loadDataHD: {loadDataHD}, renderHD: {row.renderHD}, renderHD: {row.render}')

except FileNotFoundError:
    print(f"文件未找到: {o_file}")
except pd.errors.EmptyDataError:
    print("文件为空")
except pd.errors.ParserError:
    print("文件解析错误")
except Exception as e:
    print(f"读取文件时发生错误: {e}")


