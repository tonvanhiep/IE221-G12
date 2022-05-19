from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('sanpham/<str:danhmuc>', views.sanpham, name='sanpham'),
   path('sanpham/', views.allsanpham, name='allsanpham'),
   path('chitietsanpham/<int:id>', views.chitietsanpham, name='chitietsanpham'),
   path('giohang/', views.giohang, name='giohang'),
   path('dathang/', views.dathang, name='dathang'),
   path('timkiem/', views.timkiem, name='timkiem'),
   path('danhsachyeuthich/', views.danhsachyeuthich, name='danhsachyeuthich'),
   path('dathang/camon/', views.thanks, name='camon')
]