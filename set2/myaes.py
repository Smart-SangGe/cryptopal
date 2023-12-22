@staticmethod
def new(key, mode, *args, **kwargs):
    return AESCipher(key, mode, *args, **kwargs)

MODE_ECB = 1        #: Electronic Code Book (:ref:`ecb_mode`)
MODE_CBC = 2        #: Cipher-Block Chaining (:ref:`cbc_mode`)
MODE_CFB = 3        #: Cipher Feedback (:ref:`cfb_mode`)
MODE_OFB = 5        #: Output Feedback (:ref:`ofb_mode`)
MODE_CTR = 6        #: Counter mode (:ref:`ctr_mode`)
MODE_OPENPGP = 7    #: OpenPGP mode (:ref:`openpgp_mode`)
MODE_CCM = 8        #: Counter with CBC-MAC (:ref:`ccm_mode`)
MODE_EAX = 9        #: :ref:`eax_mode`
MODE_SIV = 10       #: Synthetic Initialization Vector (:ref:`siv_mode`)
MODE_GCM = 11       #: Galois Counter Mode (:ref:`gcm_mode`)
MODE_OCB = 12       #: Offset Code Book (:ref:`ocb_mode`)

# Size of a data block (in bytes)
block_size = 16

class AESCipher:
    def __init__(self, key, mode, *args, **kwargs):
        self.key = key
        self.mode = mode
        self.key_size = (16, 24, 32)
        self.iv = kwargs.get('iv', None)
        self.nonce = kwargs.get('nonce', None)
        
    def pad(self, data: bytes, block_size: int = block_size) -> bytes:
        """Apply PKCS#7 padding to the given data."""
        padding_size = block_size - (len(data) % block_size)
        padding = bytes([padding_size] * padding_size)
        return data + padding
    
    def unpad(self, data: bytes, block_size: int = block_size) -> bytes:
        """Remove PKCS#7 padding from the given data."""
        padding_size = data[-1]
        if padding_size > block_size or padding_size == 0:
            raise ValueError('Invalid padding')
        padding = bytes([padding_size] * padding_size)
        if data[-padding_size:] != padding:
            raise ValueError('Invalid padding')
        return data[:-padding_size]
    
    def encrypt(self, plaintext: bytes) -> bytes:
        if self.mode == 1:
            return self.EBC_encrypt(plaintext)
        elif self.mode == 2:
            return self.CBC_encrypt(plaintext, self.iv)
        else:
            raise ValueError("Incorrect mode")

    def decrypt(self, ciphertext: bytes) -> bytes:
        if self.mode == 1:
            return self.EBC_decrypt(ciphertext)
        elif self.mode == 2:
            return self.CBC_decrypt(ciphertext, self.iv)
        else:
            raise ValueError("Incorrect mode")

    def EBC_encrypt(self, plaintext: bytes) -> bytes:
        ciphertext = 1
        return ciphertext

    def EBC_decrypt(self, ciphertext: bytes) -> bytes:
        plaintext = 1
        return plaintext
    
    def CBC_encrypt(self, plaintext: bytes, iv: bytes) -> bytes:
        ciphertext = 1
        return ciphertext

    def CBC_decrypt(self, ciphertext: bytes, iv: bytes) -> bytes:
        plaintext = 1
        return plaintext
    
    