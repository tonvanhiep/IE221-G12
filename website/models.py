import email
from email.mime import image
from socket import SO_DONTROUTE
from tkinter import CASCADE
from django.db import models
from sqlalchemy import false, null

# Create your models here.
class SanPham(models.Model):
#    anhsp = models.CharField(max_length=100, default='../../static/images/bantra.jpg')
    image = models.ImageField(null=True)
    giasp = models.IntegerField(null=False)
    tensp = models.CharField(max_length=100, null=False)
    thongtin = models.TextField()
    mota = models.TextField()
    danhmuc = models.CharField(max_length=30, default='sanpham')
    ngaytao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tensp


class BinhLuan(models.Model):
    idsp = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    hoten = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=30, null=False)
    noidung = models.TextField(null=False)
    ngaytao = models.DateTimeField(auto_now_add=True)


class DonHang(models.Model):
    hoten = models.CharField(max_length=30, null=False)
    sodt = models.CharField(max_length=15, null=False)
    diachi = models.TextField(null=False)
    tienhang = models.IntegerField(default=0)
    phivanchuyen = models.IntegerField(default=0)
    tongtien = models.IntegerField(default=0)
    ngaytao = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=30, null=True)
    motadh = models.TextField(null=True)


class ChiTietDH(models.Model):
    iddh = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    idsp = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    sl = models.IntegerField()