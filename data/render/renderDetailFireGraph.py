import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# 读取CSV文件
# df = pd.read_csv('/Users/matt/Downloads/卡顿问题/firegraph/graphRenderDetailHD.csv')
df = pd.read_csv('/Users/matt/Documents/vwork/1210/graphRenderDetailHD.csv')

# 将DataFrame转换为字典
data = df.to_dict(orient='list')
# data = df.to_dict(orient='list')

# 打印data字典查看结果
# print(data)


# 你的数据
# data = {
#     'total': [0, 1, 2, 3, 4, 5],
#     'openglInit': [14291.0, 12905.0, 99977.0, 2851.0, 31257.0, 11149.0],
#     'loadDataHD': [11739.0, 10693.0, 26905.0, 1197.0, 29299.0, 9291.0],
#     'renderHD': [8.0, 6.0, 8.0, 6.0, 8.0, 7.0],
#     'popOver': [2172.0, 1865.0, 71704.0, 1380.0, 1683.0, 1545.0]
# }

# 将数据转换为列表，每个子列表包含所有行的同一列的值
categories = list(data.keys())[1:]  # 排除 'index' 列
values = [data['index']] + [data[key] for key in categories]

# 创建柱状火焰图
fig, ax = plt.subplots()
bottom = [0] * len(data['index'])  # 初始化底部高度为0

# 为每个类别绘制堆叠条形
for i, (category, values) in enumerate(zip(categories, values[1:])):
    ax.bar(data['index'], values, bottom=bottom, label=category)
    bottom = [b + v for b, v in zip(bottom, values)]  # 更新底部高度

font  = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
# 添加标签和标题
ax.set_xlabel('数量', fontproperties=font)
ax.set_ylabel('耗时 (us)', fontproperties=font)
ax.set_title('渲染元素耗时火焰图', fontproperties=font)
ax.legend()

# 显示图表
plt.show()
