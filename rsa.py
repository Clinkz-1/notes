from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64


# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

# master的秘钥对的生成
private_pem = rsa.exportKey()

with open('private.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('public.pem', 'wb') as f:
    f.write(public_pem)




message = 'hello world'
with open('public.pem',"r") as f:
     key = f.read()
     rsakey = RSA.importKey(key)  # 导入读取到的公钥
     cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
     cipher_text = base64.b64encode(cipher.encrypt(message.encode(encoding="utf-8")))  # 通过生成的对象加密message明文，注意，在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
     print(cipher_text)

with open('private.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)  # 导入读取到的私钥
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    text = cipher.decrypt(base64.b64decode(cipher_text), "ERROR")  # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
    print(text)
