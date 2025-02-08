
import threading
import chardet


# 假设你有一个 UTF-8 编码的字符串
# 首先将 UTF-8 编码的字符串解码为 Unicode
unicode_string_encode1 = b'\346\267\236\350\231\271\350\267\257\346\227\251\347\217\255\350\275\246'
unicode_string_encode2 = b'\347\245\201\350\277\236\345\261\261\345\215\227\350\267\257\346\231\232\347\217\255\350\275\246'
# unicode_string_encode = b'\346\267\236\350\231\271\350\267\257\346\227\251\347\217\255\350\275\246'
# unicode_string_encode = b'\346\274\224\347\244\272\350\267\257\347\272\277'
unicode_string1 = unicode_string_encode1.decode('utf-8')
print(1,unicode_string1)
unicode_string2 = unicode_string_encode2.decode('utf-8')
print(2,unicode_string2)
