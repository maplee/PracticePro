import hashlib

def hash_string(s):
    # 创建一个新的sha256 hash对象
    hash_object = hashlib.sha256(s.encode())
    # 获取十六进制编码的哈希值
    hex_dig = hash_object.hexdigest()
    # 返回前8个字符
    return hex_dig[:8]

# 示例
original_string = "78"
hashed = hash_string(original_string)
print(hashed)