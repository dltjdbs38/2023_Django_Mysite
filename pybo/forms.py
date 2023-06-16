from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    class Meta: 
        model = Question # 속성 오버라이딩 해주기 - 클래스 안에 또 클래스
        fields = ["subject","content"]
        # widgets = { # forms.as_p 를 default가 아닌 우리 맘대로 HTML 문법을 지정
        #     "subject": forms.TextInput(attrs= {"class":"form-control"}),
        #     "content": forms.Textarea(attrs= {"class":"form-control", "rows":10}),
        # }
        # labels = {
        #     "subject" : "제목을 입력하세요!!",
        #     "content" : "내용을 입력해보세요!!"
        # }