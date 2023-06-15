# 새로 생성. pybo 만의 urls 
from django.urls import path # 경로를 이용하기 위한 
from . import views # . 은 위치 

app_name = 'pybo'

urlpatterns = [ # 이미 :8000/pybo/로 들어옴
    path("", views.index, name='index'),  
    path("<int:q_id>/", views.detail, name='detail'), # pybo/1 로 가도록 q_id라는 내 URL 변수를 만든 것이다. 
    # 그리고 views.py 의 detail 함수에 연결해 줄 것이다.
]
