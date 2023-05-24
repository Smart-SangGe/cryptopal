'''
Author: Smart-SangGe 2251250136@qq.com
Date: 2023-05-23 22:20:41
LastEditors: Smart-SangGe 2251250136@qq.com
LastEditTime: 2023-05-23 22:21:08
FilePath: \cryptopal\set1\2.py
Description: 2
'''
import binascii

def xor_hex_strings(hex1, hex2):
    # 解码十六进制字符串为字节
    bytes1 = binascii.unhexlify(hex1)
    bytes2 = binascii.unhexlify(hex2)

    # 进行XOR操作
    xor_bytes = bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])

    # 将结果编码回十六进制字符串
    xor_hex = binascii.hexlify(xor_bytes).decode()

    return xor_hex

if __name__=='__main__':
    hex1 = '1c0111001f010100061a024b53535009181c'
    hex2 = '686974207468652062756c6c277320657965'

    result = xor_hex_strings(hex1, hex2)
    print(result)
