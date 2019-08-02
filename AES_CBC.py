import string
import random
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class AES_CBC:
    def __init__(self,key='1',iv='1'):
        if len(key) % 16:
            self.key = ''.join(random.sample(string.ascii_letters+string.digits,16)).encode()
        else:self.key = key.encode()
        if len(iv) % 16:
            self.iv = ''.join(random.sample(string.ascii_letters+string.digits,16)).encode()
        else:self.iv = iv.encode()
        self.mode = AES.MODE_CBC

    def get_key(self):
        with open('./key.txt','w')as f:
            contant = f'key:{self.key.decode()}\niv:{self.iv.decode()}'
            f.write(contant)
        return (self.key.decode(),self.iv.decode())

    # 如果text不足16位的倍数就用空格补足为16位
    def add_to_16(self,text):
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode()) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode()

    # 加密函数
    def encrypt(self,text):
        text = self.add_to_16(text)
        cryptos = AES.new(self.key, self.mode, self.iv)
        cipher_text = cryptos.encrypt(text)
        # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
        return b2a_hex(cipher_text)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self,text):
        cryptos = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptos.decrypt(a2b_hex(text))
        return plain_text.decode().rstrip('\0')

if __name__ == '__main__':
    key = 'ln4ANtPM2QobI6ew'
    iv = 'VGjm2SHWEg4keDAT'

    a = AES_CBC(key,iv)
    temp = a.encrypt('hello')
    print(temp)
    print(a.decrypt(temp))
