import pandas as pd

# 读取CSV文件
file_path = '/Users/matt/Downloads/自动驾驶系统健康率看板_表1 (3).csv'  # 请根据实际路径修改
# 尝试不同的编码格式
data = pd.read_csv(file_path, encoding='GBK')

# 根据flt_name分组并汇总flt_duration
summary = data.groupby('flt_name')['flt_duration'].sum().reset_index()
# 按照flt_duration从大到小排序
summary = summary.sort_values(by='flt_duration', ascending=False)
# 输出汇总结果
print(summary)

# 如果需要将结果保存为新的CSV文件，可以使用以下代码
summary.to_csv('/Users/matt/Downloads/汇总结果.csv', index=False)