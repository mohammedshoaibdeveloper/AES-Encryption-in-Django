from django.db import models
from rest_framework import serializers

gender=(
    ("male","Male"),
    ("female","Female"),
)
# Create your models here.
class Health_Professional_Account(models.Model):
    Health_Professional_Id = models.AutoField(primary_key=True)
    Full_Name=models.CharField(max_length=100, default="")
    First_Name=models.CharField(max_length=100, default="Full_Name")
    Last_Name=models.CharField(max_length=100, default="Full_Name")
    Email=models.CharField(max_length=100, default="")
    Username=models.CharField(max_length=100, default="")
    Gender=models.CharField(max_length=100, choices=gender,default="male")
    Date_of_Birth=models.CharField(max_length=200, default="Full_Name")
    Password=models.CharField(max_length=3000, default="")
    Degree=models.CharField(max_length=200, default="Full_Name")
    Affiliation=models.CharField(max_length=200, default="Full_Name")
    Bio=models.TextField(default="Full_Name")
    Street_Address=models.CharField(max_length=500, default="Full_Name")
    City=models.CharField(max_length=500, default="Full_Name")
    State=models.CharField(max_length=500, default="Full_Name")
    Country=models.CharField(max_length=500, default="Full_Name")
    Location=models.CharField(max_length=500, default="Full_Name")
    Role=models.CharField(max_length=100,default="earhealthprofessional")
    Health_Professional_Image=models.ImageField(upload_to='Health_Professional/',default="Health_Professional/dummy.jpg")
    Mobile_Number = models.CharField(max_length=200, default="Full_Name")
    Email_Verification_Code = models.CharField(max_length=200, default="Full_Name")
    OTP_Verification = models.CharField(max_length=200, default="12345")
    Doctor_rating = models.IntegerField(default=0)
    Doctor_rating_Count = models.IntegerField(default=0)


    



    def __str__(self):
        return self.Full_Name

class SerHealth_Professional_Account(serializers.ModelSerializer):
    class Meta:
        model = Health_Professional_Account
        
        fields = '__all__'