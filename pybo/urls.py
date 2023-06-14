# 새로 생성. pybo 만의 urls 
from django.urls import path # 경로를 이용하기 위한 
from . import views # . 은 위치 

urlpatterns = [ # 이미 :8000/pybo/로 들어옴
    path("", views.index),  # 
]
