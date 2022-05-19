from django import forms
from .models import TaiKhoan


class FormDangKi(forms.ModelForm):
    class Meta:
        model = TaiKhoan
        fields = ('tendn', 'email', 'sodt', 'matkhau', 'diachi', 'hoten',)
        widgets = {
            'tendn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên đăng nhập (*)'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email (*)'}),
            'sodt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại', 'required':'False',}),
            'matkhau': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mật khẩu (*)'}),
            'diachi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Địa chỉ', 'required':'False',}),
            'hoten': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Họ và tên', 'required':'False',}),
        }