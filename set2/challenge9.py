"""
PKCS#7 padding is a byte-padding scheme that pads the 
input data to a specific block length by appending N 
bytes of value N, where N is the number of bytes required 
to reach the desired block size.
"""


def pkcs7_pad(data: bytes, block_size: int) -> bytes:
    """Apply PKCS#7 padding to the given data."""
    padding_size = block_size - (len(data) % block_size)
    padding = bytes([padding_size] * padding_size)
    return data + padding

def pkcs7_unpad(data: bytes, block_size: int) -> bytes:
    """Remove PKCS#7 padding from the given data."""
    padding_size = data[-1]
    if padding_size > block_size or padding_size == 0:
        raise ValueError('Invalid padding')
    padding = bytes([padding_size] * padding_size)
    if data[-padding_size:] != padding:
        raise ValueError('Invalid padding')
    return data[:-padding_size]

# Example usage:
data = b"Hello, world??"
block_size = 16

# Pad the data
padded_data = pkcs7_pad(data, block_size)
print(padded_data)

# Unpad the data
unpadded_data = pkcs7_unpad(padded_data, block_size)
print(unpadded_data)
