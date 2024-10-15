import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt(crypt: str) -> str:
    key = [8, 20, 157, 167, 60, 89, 206, 98, 85, 91, 1, 233, 47, 52, 232, 56]
    iv = [210, 187, 27, 253, 232, 59, 56, 195, 68, 54, 99, 87, 183, 156, 174, 28]
    data = base64.urlsafe_b64decode(crypt)
    aes = AES.new(bytes(key), AES.MODE_CBC, bytes(iv))
    data_decrypt = aes.decrypt(data)
    result = unpad(data_decrypt, AES.block_size).decode()
    return result
