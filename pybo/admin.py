from django.contrib import admin
from pybo.models import Question,Answer # 수정
# Register your models here.
class QuestionSearch(admin.ModelAdmin): # 검색 기능 추가
    search_fields = ['subject','create_date'] # 상속받은 것. _가 나오면 다른 클래스를 상속받은 거다. 외래키 _set처럼
    # 'subject','create_date' 는 검색하고자 하는 Question 모델의 컬럼명
    # search_fields 는 우리가 지은 변수이름이 아니고 ModelAdmin에서 제공하는 듯?
admin.site.register(Question, QuestionSearch) # 관리자 페이지를 구성할 수 있게 해준다. 
admin.site.register(Answer)

