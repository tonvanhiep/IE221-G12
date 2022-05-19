from genericpath import exists
from cherrypy import url
from django.shortcuts import render
from django.http import HttpResponse
from sqlalchemy import null
from .models import TaiKhoan
from .form import FormDangKi
from django.http import HttpResponseRedirect

# Create your views here.

def dangnhap(request):
   return render(request, 'pages/dangnhap.html')

def dangki(request):
   dk = FormDangKi()
   if request.method == "POST":
      dk = FormDangKi(request.POST)
      if dk.is_valid():
         dk.save()
         return HttpResponseRedirect(url='home')
      else:
         return HttpResponse("Loi")
   return render(request, 'pages/dangki.html', {"f_dk": dk})

