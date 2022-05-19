from django.contrib import admin
from .models import TaiKhoan

# Register your models here.
class TaiKhoan_Admin(admin.ModelAdmin):
    list_display = ['tendn', 'email', 'sodt', 'ngaytao']

admin.site.register(TaiKhoan, TaiKhoan_Admin)