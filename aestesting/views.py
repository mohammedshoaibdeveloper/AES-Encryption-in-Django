from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
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

from aestesting.models import Health_Professional_Account,SerHealth_Professional_Account

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



class User_Signup(APIView):

    def get(self,request):

        doctor = Health_Professional_Account.objects.get()
        Email = doctor.Email
        Username = doctor.Username
        Full_Name = doctor.Full_Name
        Password = doctor.Password
        Email = cipher.decrypt(Email)
        Username = cipher.decrypt(Username)
        Full_Name = cipher.decrypt(Full_Name)
        Password = cipher.decrypt(Password)
      
        # serializer = SerHealth_Professional_Account(doctor,many=True)
        message={

            "Email":Email,
            "Username":Username,
            "Full_Name":Full_Name,
            "Password":Password,

            
            
        }
        return Response(message)

    # def post(self,request):

    #     Email=request.data.get('Email')
    #     Email = cipher.encrypt(Email)
    #     Username=request.data.get('Username')
    #     Username = cipher.encrypt(Username)
    #     # Mobile_Number = request.data.get('Mobile_Number')
    #     # Mobile_Number = cipher.encrypt(Mobile_Number)
    #     Full_Name = request.data.get('Full_Name')
    #     Full_Name = cipher.encrypt(Full_Name)
    #     Password = request.data.get('Password')
    #     Password = cipher.encrypt(Password)


    #     data = Health_Professional_Account(Email=Email,Username=Username,Full_Name=Full_Name,Password=Password)
    #     message = {

    #         'Email': Email,
    #         'Username': Username,
    #         # 'Mobile_Number': Mobile_Number,
    #         'Full_Name': Full_Name,
    #         'Password': Password,


    #     }
    #     data.save()
    #     return Response(message)

    def post(self,request):
        Email=request.data.get('Email')
        Email = str(cipher.encrypt(Email))
        Email=Email[2:-1]
   


        Username=request.data.get('Username')
        Username = str(cipher.encrypt(Username))
        Username=Username[2:-1]
   

        Full_Name = request.data.get('Full_Name')
        Full_Name = str(cipher.encrypt(Full_Name))
        Full_Name=Full_Name[2:-1]


        Password = request.data.get('Password')
        Password = str(cipher.encrypt(Password))
        Password=Password[2:-1]



        data = Health_Professional_Account(Email=Email,Username=Username,Full_Name=Full_Name,Password=Password)
        message = {

            'message' : "successfully"
            
          


        }
        data.save()
        return Response(message)


class SerData(APIView):

    def get(self,request):

        doctor = Health_Professional_Account.objects.all()
        serializer = SerHealth_Professional_Account(doctor,many=True)
        message={

            'status' : True,
            'data':serializer.data
            
        }
        return Response(message)