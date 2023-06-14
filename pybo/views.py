from django.shortcuts import render
from django.http import HttpResponse # 추가
# Create your views here.

def index(request): # 추가 - 실제 사용자에게 보여지는 공간. request는 clien의 요청
    return HttpResponse("pybo에서 응답해줄 내용")

