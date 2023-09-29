import binascii

with open("set1/4.txt",'r') as file:
    lines = file.readlines()

hex_str = "".join(line.strip() for line in lines)
bytes_str = binascii.unhexlify(hex_str)

for key in range(256):
    decrypted = "".join(chr(b ^ key) for b in bytes_str)
print(decrypted)

# 不知道为什么全部都是乱码