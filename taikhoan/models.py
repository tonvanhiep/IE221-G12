import email
from socket import SO_DONTROUTE
from django.db import models

# Create your models here.
class TaiKhoan(models.Model):
    tendn = models.CharField(max_length=20, primary_key=True)
    email = models.CharField(max_length=30, null=False)
    sodt = models.CharField(max_length=15)
    matkhau = models.CharField(max_length=20, null=False)
    diachi = models.TextField(max_length=200)
    hoten = models.CharField(max_length=30)
    ngaytao = models.DateTimeField(auto_now_add=True)
