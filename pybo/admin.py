from django.contrib import admin
from pybo.models import Question # 수정
# Register your models here.
admin.site.register(Question) # 웹 페이지를 구성할 수 있게 해준다. 