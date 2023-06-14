# Django의 장점 : ORM(Object Relative Model) 
#     - SQL 문법을 안 쓰고도 데이터베이스를 관리?할 수 있는 
#     → models.py 에서 Class로 DB안에 테이블을 만들어줄 수 있다.
from django.db import models

# sqllite 는 RDBMS다. 
#   테이블1 - question - subject, content, create_date 컬럼 정의
#   테이블2 - answer - question(외래키), content, create_date
class Question(models.Model): # 테이블 이름 = 클래스명  
    subject = models.CharField(max_length=200) 
    content = models.TextField() # Char와 Text의 차이 = max_length로 글자제한 vs 무한 가능
    create_date = models.DateTimeField()

    def __str__(self): 
        return self.subject # shell에서 Question.objects.all()하면 subject 로 표현해줌.

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE) # 외래키 : 외부에 있는 테이블을 가져와서 컬럼처럼 사용
    # on_delete = 그 연결된 question이 지워지면, answer도 지울거야? ㅇㅇ 
    content = models.TextField()
    create_date = models.DateTimeField()