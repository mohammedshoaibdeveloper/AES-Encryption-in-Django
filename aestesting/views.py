from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect

# from Crypto.Cipher import AES
# import hashlib

# password = "mypassword".encode()
# key = hashlib.sha256(password).digest()
# mode = AES.MODE_CBC
# IV = 'This is an IV456'

# def pad_message(message):
#   while len(message)%16 !=0:
#     message = message + " "
#   return message

# cipher = AES.new(key,mode,IV)

# cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, IV.encode("utf8"))
# message = "This is my message"
# padded_message = pad_message(message)
# encrypted_message  = cipher.encrypt(padded_message)

# print(message)
# print(padded_message)
# print(encrypted_message)


# def index(request):
#     return HttpResponse("ok")


from hashlib import sha256
import base64
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]

class AESCipher:

    def __init__( self, key ):
        self.key = bytes(key, 'utf-8')

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode('utf8')

cipher = AESCipher('mysecretpassword')
encrypted = cipher.encrypt('11/5/2020')
decrypted = cipher.decrypt(encrypted)

print(encrypted)
print(decrypted)

