
def repeating_key_xor(key, message):
    key_length = len(key)
    message_length = len(message)
    expanded_key = (key * (int(message_length / key_length))) + key[:message_length % key_length]
    return bytes([m ^ k for m, k in zip(message, expanded_key)])

message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

# Convert message and key to bytes
message = message.encode('utf-8')
key = key.encode('utf-8')

cipher = repeating_key_xor(key, message)

# Convert to hexadecimal
cipher_hex = cipher.hex()

print(cipher_hex)
