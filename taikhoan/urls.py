from django.urls import path
from . import views

urlpatterns = [
   path('', views.dangnhap, name='dangnhap'),
   path('dangnhap/', views.dangnhap),
   path('dangki/', views.dangki, name='dangki'),
]