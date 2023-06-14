"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # 다른 앱의 urls.py 통쨰로 이용하기 위해 
# from pybo import views # 추가 -> 삭제 이제 pybo urls.py로 다 넘겨버리겠다.

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pybo/", include('pybo.urls')),  # 아예 pybo의 urls.py가 다 해라. 
]
