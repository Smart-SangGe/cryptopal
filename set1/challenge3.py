'''
Author: Smart-SangGe 2251250136@qq.com
Date: 2023-05-24 14:00:42
LastEditors: Smart-SangGe 2251250136@qq.com
LastEditTime: 2023-05-24 14:05:11
FilePath: \cryptopal\set1\3.py
Description: 3
'''
import binascii

hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
bytes_str = binascii.unhexlify(hex_str)
print(bytes_str)
for key in range(256):
    decrypted = "".join(chr(b ^ key) for b in bytes_str)
    print(f"{key}: {decrypted}")
# 88: Cooking MC's like a pound of bacon