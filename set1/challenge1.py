'''
Author: Smart-SangGe 2251250136@qq.com
Date: 2023-05-23 22:17:57
LastEditors: Smart-SangGe 2251250136@qq.com
LastEditTime: 2023-05-23 22:18:36
FilePath: \cryptopal\set1\1.py
Description: 1
'''
import binascii
import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
binary_string = binascii.unhexlify(hex_string)
base64_string = base64.b64encode(binary_string)

print(base64_string.decode())  # 解码为字符串以便打印
