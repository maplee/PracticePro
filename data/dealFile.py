import os

def delete_files_with_keyword(directory, keyword):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword in file:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

# 使用示例
directory = "/Users/matt/Desktop/hengyang_1qi"  # 要删除文件的目录路径

keyword = "zebra"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "greenbelts"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "isolationbelt"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "trafficlight"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "trafficsign"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "trafficdenoter"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "diversion"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "roadsideequipments"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "alphanumeric"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "cable"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "opticalcable"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "camera"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
keyword = "safetyisland"  # 包含特定字段的关键词
delete_files_with_keyword(directory, keyword)
