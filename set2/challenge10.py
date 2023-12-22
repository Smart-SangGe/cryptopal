import myaes


def encrypt_ecb(plaintext: bytes, key: bytes) -> bytes:
    cipher = myaes.new(key, myaes.MODE_ECB)
    padded_plaintext = cipher.pad(plaintext, myaes.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_ecb(ciphertext: bytes, key: bytes) -> bytes:
    cipher = myaes.new(key, myaes.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = cipher.unpad(padded_plaintext, myaes.block_size)
    return plaintext

# Example Usage:
key = b'YELLOW SUBMARINE'
plaintext = b'Hello, World!'

# Encrypt the plaintext
ciphertext = encrypt_ecb(plaintext, key)
print(ciphertext)

# Decrypt the ciphertext
decrypted_plaintext = decrypt_ecb(ciphertext, key)
print(decrypted_plaintext)
