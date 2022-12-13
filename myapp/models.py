from django.db import models
from django.contrib.auth.models import User
import uuid
from django_resized import ResizedImageField


# Create your models here.
GENDER_CHOICE = [
    ('M', 'MALE'),
    ('F', 'FEMALE'),
]

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE,related_name='profile')
    mobile_no = models.CharField(max_length=20)
    otp = models.CharField(max_length=50, null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4)
    
STATE_CHOICE = (
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Chandigarh","Chandigarh"),
    ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),
    ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
    ("Puducherry","Puducherry"))
  

class DirivingLicence(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField( auto_now=False, auto_now_add=False)
    place_of_birth = models.CharField(max_length=50)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICE,max_length=255,null=True, blank=True)
    zipcode = models.IntegerField() 
    image = ResizedImageField(upload_to='profile_pic',size=[500,300],crop=['middle','center'],force_format='JPEG')
