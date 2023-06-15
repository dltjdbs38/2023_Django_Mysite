# from django.http import HttpResponse # 추가
from django.shortcuts import render # render : template에게 컨텐츠를 전달하는 함수. template : 사용자에게 보여주기 위해 html
from pybo.models import Question
# def index(request): # 추가 - 실제 사용자에게 보여지는 공간. request는 clien의 요청
#     return HttpResponse("pybo에서 응답해줄 내용")

### views.py는 client와 template의 중간자 역할. 데이터를 넘겨주고, 정의하는 부분


# 우리는 오늘 DB와 연동한 template를 사용자에게 보여줄 것이다.
def index(request): # 사용자로부터 인자를 받자(요청 = request)
    question_list = Question.objects.order_by('-create_date') # DB의 objects를 가져와서 시간순 정렬
    # order_by default는 내림차순, 우리는 최근부터 보여줘야하니까 오름차순으로 -
    context = {'question_list' : question_list} # dict로 포장해서 사용자에게 보내주기
    return render(request, 'pybo/question_list.html', context) # 요청, template 경로, 보여줄내용

