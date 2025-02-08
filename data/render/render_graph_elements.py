import csv
import re
import os
import pandas as pd
import math

# 原始数据
log_file_path = "/Users/matt/Downloads/卡顿问题/log1119_1.txt"
# log_file_path = "/Users/matt/Downloads/log1120.txt"
# log_file_path = "/Users/matt/Downloads/log1120_1.txt"
# log_file_path = "/Users/matt/StudioProjects/map_core/log1114_1.txt"
log_file_path = "/Users/matt/Documents/vwork/1203/log1203_1.txt"
log_file_path = "/Users/matt/Documents/vwork/1205/log1205_4.txt"
log_file_path = "/Users/matt/Documents/vwork/1209/log1209_2.txt"
logfile = open(log_file_path, 'r')

# 准备CSV文件的标题行
csv_headers = []

# 准备写入CSV的数据列表
csv_data_dict = {}
data_list = []
# 标记是否是数据行
is_data_line = True

# 获取文件所在的目录
directory = os.path.dirname(log_file_path)

o_file = os.path.join(directory,'output.csv')
# csvfile = open(o_file, 'w')
# writer = csv.writer(csvfile)
isHead=True

# 创建一个空的DataFrame，预定义列名
df = pd.DataFrame(columns=[])


with open(log_file_path, 'r') as file:
    for line in file:
        if line.__contains__('MapEngine::render-start'):
            is_data_line = True
        if line.__contains__('MapEngine-ttop-render--over'):
            is_data_line = False

        # 使用正则表达式提取数据
        match = re.match(r'.+?ttop-(.+?)--over:(\d+)', line)
        if match:
            title, value = match.groups()
            title = title.replace('-', '_').replace(':', '_').replace('_PainterMgr', 'PainterMgr').replace('.', '_')
            if is_data_line:
                # csv_data_dict[title] = value
                vv = csv_data_dict.get(title, '')
                # print(title,vv)
                if vv in [None, '']:
                    if isHead:
                        csv_headers.append(title)
                    csv_data_dict[title] = int(value)
                else :
                    csv_data_dict[title] += int(value)
                # start ------------
                # if isHead:
                #     csv_headers.append(title)
                # csv_data_dict[title] = value
                # over ------------
            else:
                csv_data_dict['render'] = value
                readyV = csv_data_dict.get('ready', '')
                if readyV in [None, '']:
                    continue
                dividerV = csv_data_dict.get('divider', '')
                if dividerV in [None, '']:
                    continue
                data_list.append(csv_data_dict)
                if isHead:
                    csv_headers.append('render')
                # start------------
                # csv_data_dict['render'] = value
                # if isHead:
                #     csv_headers.append('render')
                #     df = pd.DataFrame.from_dict(csv_data_dict, orient='index') #,columns=csv_headers
                # else:
                #     df = df.append(csv_data_dict, ignore_index=True)
                # over ------------
                csv_data_dict = {}
                isHead = False
        # else:
            # print(line)
    df = pd.DataFrame(data_list)
    df = df[csv_headers]
    df.to_csv(o_file, index=True, encoding='utf-8')



# graphTotalCsv = '/Users/matt/Downloads/卡顿问题/firegraph/graphTotal.csv'
# graphLoadHDCsv = '/Users/matt/Downloads/卡顿问题/firegraph/graphLoadHD.csv'
# graphRenderHDCsv = '/Users/matt/Downloads/卡顿问题/firegraph/graphRenderHD.csv'
# graphRenderDetailHDCsv = '/Users/matt/Downloads/卡顿问题/firegraph/graphRenderDetailHD.csv'

graphTotalCsv = os.path.join(directory,'graphTotal.csv')
graphLoadHDCsv = os.path.join(directory,'graphLoadHD.csv')
graphRenderHDCsv = os.path.join(directory,'graphRenderHD.csv')
graphRenderDetailHDCsv = os.path.join(directory,'graphRenderDetailHD.csv')


#total
t_dict = {}
t_list = []
dfTotal = pd.DataFrame(columns=[])

#loadHD
loadHD_dict = {}
loadHD_list = []
dfLoadHD = pd.DataFrame(columns=[])

#renderHD
renderHD_dict = {}
renderHD_list = []
dfRenderHD = pd.DataFrame(columns=[])

#renderDetailHD
renderDetailHD_dict = {}
renderDetailHD_list = []
dfrenderDetailHD = pd.DataFrame(columns=[])

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
        loadDataHD_ready = row.loadDataHD_ready

        openglInit =  row.loadDataHD - row.QLayerMgr__loadDataHD - row.loadDataHD_ready


        total = row.ready + row.loadDataHD + row.renderHD + row.render

        openglInit = row.setMat
        total = row.ready + row.loadDataHD + row.renderHD + row.render + openglInit
        if total == 0:
            continue
        if math.isnan(total):
            continue
        # 打印每一行的数据
        # print(f'{row.Index},total: {total}, openglInit: {openglInit}, loadDataHD: {row.QLayerMgr__loadDataHD}, renderHD: {row.renderHD}, popOver: {row.render}')
        t_dict['total'] = total
        t_dict['openglInit'] = openglInit
        t_dict['loadDataHD'] = row.QLayerMgr__loadDataHD
        t_dict['renderHD'] = row.renderHD
        t_dict['popOver'] = row.render
        t_list.append(t_dict)
        t_dict = {}

        # renderHD_dict['skybox'] = row.onRender3dPass2_skybox
        RenderElements = row.onRender3dPass2_skybox+row.onRender3dPass2_Plane+row.onRender3dPass2_Weather+row.onRender3dPass2_StreetLight +row.onRender3dPass2_Style+row.onRender3dPass2_guideline+row.onRender3dPass2_lightwave+row.onRender3dPass2_ice+row.onRender3dPass2_water+row.onRender3dPass2_SignalLine\
                         +row.skybox+row.plane+row.greenBelt+row.roadbed+row.zebra+row.diversion+row.divider+row.divider_texture+row.safetyIsland\
                         +row.onRenderPass2Order3_skybox+row.onRenderPass2Order3_Plane+row.onRenderPass2Order3_Weather+row.onRenderPass2Order3_StreetLight+row.onRenderPass2Order3_Style+row.onRenderPass2Order3_guideline\
                         +row.onRenderPass2Order3_lightwave+row.onRenderPass2Order3_ice+row.onRenderPass2Order3_water+row.onRenderPass2Order3_SignalLine\
                         +row.renderPost+row.PainterMgr__render
        renderScene = row.skybox+row.plane+row.greenBelt+row.roadbed+row.zebra+row.diversion+row.divider+row.divider_texture+row.safetyIsland
        RenderDetail = row.PainterMgr__drawHDMap_render+row.Anchor+row.PrimitiveScenedraw+row.drawCustomElement+row.renderTransparent+row.renderTransparentAnchor
        # print(f'RenderElements:{RenderElements},{row.PainterMgr__drawHDMap_render},renderScene:{renderScene},{row.renderScene},RenderDetail:{RenderDetail},renderTotal:{row.renderHD},{row.renderHD-RenderDetail}')
        renderHD_dict['elmments'] = RenderDetail
        renderHD_dict['others'] = row.renderHD-RenderDetail
        renderHD_list.append(renderHD_dict)
        renderHD_dict = {}

        renderDetailHD_dict['skybox'] = row.onRender3dPass2_skybox + row.skybox + row.onRenderPass2Order3_skybox
        renderDetailHD_dict['plane'] = row.onRender3dPass2_Plane + row.plane + row.onRenderPass2Order3_Plane
        renderDetailHD_dict['weather'] = row.onRender3dPass2_Weather + row.onRenderPass2Order3_Weather
        renderDetailHD_dict['streetLight'] = row.onRender3dPass2_StreetLight + row.onRenderPass2Order3_StreetLight
        renderDetailHD_dict['style'] = row.onRender3dPass2_Style + row.onRenderPass2Order3_Style
        renderDetailHD_dict['guideline'] = row.onRender3dPass2_guideline + row.onRenderPass2Order3_guideline
        renderDetailHD_dict['lightwave'] = row.onRender3dPass2_lightwave + row.onRenderPass2Order3_lightwave
        renderDetailHD_dict['ice'] = row.onRender3dPass2_ice + row.onRenderPass2Order3_ice
        renderDetailHD_dict['water'] = row.onRender3dPass2_water + row.onRenderPass2Order3_water
        renderDetailHD_dict['signalLine'] = row.onRender3dPass2_SignalLine + row.onRenderPass2Order3_SignalLine
        renderDetailHD_dict['greenBelt'] = row.greenBelt
        renderDetailHD_dict['roadbed'] = row.roadbed
        renderDetailHD_dict['zebra'] = row.zebra
        renderDetailHD_dict['diversion'] = row.diversion
        renderDetailHD_dict['divider'] = row.divider + row.divider_texture
        renderDetailHD_dict['safetyIsland'] = row.safetyIsland
        renderDetailHD_list.append(renderDetailHD_dict)
        renderDetailHD_dict = {}

    dfTotal = pd.DataFrame(t_list)
    # dfTotal = dfTotal['index', 'total', 'openglInit', 'loadDataHD', 'renderHD', 'popOver']
    dfTotal.to_csv(graphTotalCsv, index=True, encoding='utf-8')
    #render
    dfRenderHD = pd.DataFrame(renderHD_list)
    # dfRenderHD = dfRenderHD['index', 'elmments', 'others']
    dfRenderHD.to_csv(graphRenderHDCsv, index=True, encoding='utf-8')
    #renderDetail
    dfRenderDetailHD = pd.DataFrame(renderDetailHD_list)
    # dfRenderDetailHD = dfRenderDetailHD['index', 'skybox', 'plane', 'weather', 'streetLight', 'style', 'guideline', 'ice', 'water', 'signalLine', 'greenBelt', 'roadbed', 'zebra', 'diversion', 'divider', 'safetyIsland']
    dfRenderDetailHD.to_csv(graphRenderDetailHDCsv, index=True, encoding='utf-8')
except FileNotFoundError:
    print(f"文件未找到: {o_file},{graphTotalCsv}")
except pd.errors.EmptyDataError:
    print("文件为空")
except pd.errors.ParserError:
    print("文件解析错误")
except Exception as e:
    print(f"读取文件时发生错误: {e}")


