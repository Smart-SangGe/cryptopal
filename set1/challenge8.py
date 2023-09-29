def detect_aes_ecb(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    ecb_encrypted_line = None
    for line_num, line in enumerate(lines):
        # Remove any trailing whitespace and decode hex to bytes
        ciphertext = bytes.fromhex(line.strip())

        # Split ciphertext into 16-byte blocks
        blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

        # Check for repeating blocks
        if len(blocks) != len(set(blocks)):
            ecb_encrypted_line = line_num + 1  # Line numbers are 1-indexed
            break

    return ecb_encrypted_line

# Usage:
filename = '8.txt'
ecb_line = detect_aes_ecb(filename)
if ecb_line:
    print(f'Line {ecb_line} is likely encrypted using AES in ECB mode.')
else:
    print('No ECB encrypted ciphertext found.')
