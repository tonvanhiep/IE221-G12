from dataclasses import fields
from logging import PlaceHolder
from tkinter import Widget
from xml.dom.minidom import Text
from django import forms
from .models import BinhLuan, DonHang


# class FormDatHang(forms.Form):
#     hoten = forms.CharField(
#         max_length=50, 
#         widget=forms.TextInput(
#             attrs={'class': 'form-control', 'PlaceHolder': 'Tôn Văn Hiệp', 'required': 'True'}))
#     sodt = forms.CharField(
#         max_length=15, 
#         widget=forms.TextInput(
#             attrs={'class': 'form-control', 'PlaceHolder': '0363038485', 'required': 'True'}))
#     diachi = forms.CharField(
#         max_length=200, 
#         widget=forms.TextInput(
#             attrs={'class': 'form-control', 'PlaceHolder': 'KTX B, Đông Hòa, Dĩ An, Bình Dương', 'required': 'True'}))


class FormBinhLuan(forms.ModelForm):
    class Meta:
        model = BinhLuan
        fields = ('hoten', 'email', 'noidung', 'idsp',)
        widgets = {
            'hoten': forms.TextInput(attrs={'id': 'hoten', 'placeholder': 'Họ tên'}),
            'email': forms.TextInput(attrs={'id': 'email', 'placeholder': 'Email'}),
            'noidung': forms.Textarea(attrs={'id': 'baidanhgia', 'placeholder': 'Bài đánh giá'}),
            'idsp': forms.TextInput(attrs={'value': ''}),
        }



class FormDatHang(forms.ModelForm):
    class Meta:
        model = DonHang
        fields = ('hoten', 'sodt', 'diachi', 'email', 'tienhang', 'phivanchuyen', 'tongtien', 'motadh',)
        widgets = {
            'hoten': forms.TextInput(attrs={'class': 'form-control', 'PlaceHolder': 'Tôn Văn Hiệp'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'PlaceHolder': 'tonvanhiepdragon@gmail.com'}),
            'sodt': forms.TextInput(attrs={'class': 'form-control', 'PlaceHolder': '0363038485'}),
            'diachi': forms.TextInput(attrs={'class': 'form-control', 'PlaceHolder': 'KTX B, Đông Hòa, Dĩ An, Bình Dương'}),
            'tienhang': forms.TextInput(attrs={'value': 0}),
            'phivanchuyen': forms.TextInput(attrs={'value': 0}),
            'tongtien': forms.TextInput(attrs={'value': 0}),
            'motadh': forms.TextInput(attrs={'value': ''})
        }