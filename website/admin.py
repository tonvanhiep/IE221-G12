from django.contrib import admin
from .models import SanPham, BinhLuan, DonHang, ChiTietDH

# Register your models here.
class SanPham_Admin(admin.ModelAdmin):
    list_display = ['id', 'tensp', 'giasp', 'danhmuc','ngaytao']

class BinhLuan_Admin(admin.ModelAdmin):
    list_display = ['hoten', 'email','ngaytao']

class DonHang_Admin(admin.ModelAdmin):
    list_display = ['hoten', 'sodt', 'tongtien','ngaytao']

class ChiTietDH_Admin(admin.ModelAdmin):
    list_display = ['iddh', 'idsp', 'sl']



admin.site.register(SanPham, SanPham_Admin)
admin.site.register(BinhLuan, BinhLuan_Admin)
admin.site.register(DonHang, DonHang_Admin)
admin.site.register(ChiTietDH, ChiTietDH_Admin)