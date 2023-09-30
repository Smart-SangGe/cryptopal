from Crypto.Util.number import *
import base64

def hamming_distance(str1: str, str2: str) -> int:
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    hamming = bin(bytes_to_long(str1) ^ bytes_to_long(str2))
    distance = 0
    for one in hamming:
        if one == '1':
            distance = distance + 1

    return distance


# a = b'this is a test'
# b = b'wokka wokka!!!'
# print(hamming_distance(a,b))

with open("set1/6.txt",'r') as file:
    lines = file.readlines()
base64_str = "".join(line.strip() for line in lines)
cipher = base64.b64decode(base64_str)

# variances = [99]
# for key_size in range(2,40):
#     # print('key_size',key_size)
#     a = hamming_distance(cipher[0: key_size], cipher[key_size:2 * key_size]) / key_size
#     b = hamming_distance(cipher[2 * key_size: 3 * key_size], cipher[3 * key_size: 4 * key_size]) / key_size
#     c = hamming_distance(cipher[4 * key_size: 5 * key_size], cipher[5 * key_size: 6 * key_size]) / key_size
#     d = hamming_distance(cipher[6 * key_size: 7 * key_size], cipher[7 * key_size: 8 * key_size]) / key_size
#     data = [a, b, c, d]
#     variances.append(statistics.variance(data))
    
# print(variances.index(min(variances)))

for keysz in range(2, 40):
    print(keysz, hamming_distance(cipher[:keysz], cipher[keysz: 2 * keysz]) * 1.0 / keysz, sum([hamming_distance(cipher[keysz * i:keysz * i + keysz], cipher[: keysz]) for i in range(10)]) * 1.0 / keysz)




# key_size = 4
# for key_size in range(1,40):
    # print(len(cipher) / key_size)
# for i in range(int(len(cipher) / key_size)):
#     for key in range(255):
#         decrypted = "".join(chr(b ^ key) for b in cipher[i * key_size: i * key_size + key_size])
#         print(decrypted)
    