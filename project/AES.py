import sys
import base64
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key):
        self.bs = 16

        if isinstance(key, str):
            key = key.encode('utf-8')
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        if isinstance(raw, str):
            raw = raw.encode('utf-8')  
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return encoded.decode('utf-8')  

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return self._unpad(decrypted).decode('utf-8')  

    def _pad(self, b):

        padding_length = self.bs - len(b) % self.bs
        padding = bytes([padding_length] * padding_length)
        return b + padding

    def _unpad(self, b):

        padding_length = b[-1]
        return b[:-padding_length]
