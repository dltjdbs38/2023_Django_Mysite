from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    class Meta: 
        model = Question # 속성 오버라이딩 해주기 - 클래스 안에 또 클래스
        fields = ["subject","content"]