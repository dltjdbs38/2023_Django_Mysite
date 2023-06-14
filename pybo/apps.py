from django.apps import AppConfig


class PyboConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField" # DB 컬럼이 자동으로 지정
    name = "pybo" # 디렉토리 이름
