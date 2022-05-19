from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import HttpResponse
from .models import SanPham, DonHang, ChiTietDH, BinhLuan
from django.http import Http404
from .form import FormBinhLuan, FormDatHang
from django.http import HttpResponseRedirect




# Create your views here.

def index(request):
   return render(request, 'pages/home.html')


def allsanpham(request):
   sanpham = SanPham.objects.all().order_by('-ngaytao')
   return render(request, 'pages/sanpham.html', {'SanPham' : sanpham})


def sanpham(request, danhmuc):
   sanpham = SanPham.objects.filter(danhmuc__contains=danhmuc)
   return render(request, 'pages/sanpham.html', {'SanPham' : sanpham})


def chitietsanpham(request, id):
   cmm = FormBinhLuan()
   if request.method == "POST":
      cmm = FormBinhLuan(request.POST)
      if cmm.is_valid():
         cmm.save()
         return HttpResponseRedirect(request.path)
   sanpham = SanPham.objects.get(id=id)
   binhluan = BinhLuan.objects.filter(idsp=id)
   return render(request, 'pages/chitietsanpham.html', {'SanPham' : sanpham, 'BinhLuan' : binhluan, 'f_cmm': cmm})


def giohang(request):
   return render(request, 'pages/giohang.html')


def dathang(request):
   dh = FormDatHang()
   if request.method == "POST":
      dh = FormDatHang(request.POST)
      if dh.is_valid():
         dh.save()
         return HttpResponseRedirect('camon')
   return render(request, 'pages/dathang.html', {'f_dh': dh})


def timkiem(request):
   query_dict = request.GET
   query = query_dict.get("sp")
   sp = SanPham.objects.filter(tensp__contains=query).order_by('-ngaytao')
   return render(request, 'pages/timkiem.html', {"SanPham": sp, "query": query})


def danhsachyeuthich(request):
   return render(request, 'pages/danhsachyeuthich.html')


def thanks(request):
    return render(request, 'pages/camonquykhach.html')


def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})




# def chitietsanpham(request, id):
#     try:
#         data = SanPham.objects.get(id=id)
#     except SanPham.DoesNotExist:
#         raise Http404("Bài viết không tồn tại")
    
#     return render(request, 'pages/chitietsanpham.html', data)