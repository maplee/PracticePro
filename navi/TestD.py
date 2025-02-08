from datetime import datetime

# 获取当前日期和时间
current_datetime = datetime.now()

# 从当前日期和时间中提取日期部分
current_date = current_datetime.date()

# 打印当前日期
print("当前日期:",  str(current_date).replace("-", ""))
