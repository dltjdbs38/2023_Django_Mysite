# 2023_Django_Mysite
2023 06 14 Django Tutorial - CCCR DevOps 반 Django 프로젝트

초기설정   
![image](https://github.com/dltjdbs38/2023_Django_Mysite/assets/74050826/6f8e98db-1234-4eeb-8a40-eae38015648a)
```
# USER@DESKTOP-MM3Q7OA MINGW64 ~/Desktop/장고튜토리얼 (master)
# $ python -m venv venv
# (base)
# USER@DESKTOP-MM3Q7OA MINGW64 ~/Desktop/장고튜토리얼 (master)
# $ ls -a
# ./   .git/       package.json       public/    src/
# ../  .gitignore  package-lock.json  README.md  venv/
(base)
USER@DESKTOP-MM3Q7OA MINGW64 ~/Desktop/장고튜토리얼 (master)
$ source ./venv/Scripts/activate
(venv) (base)
USER@DESKTOP-MM3Q7OA MINGW64 ~/Desktop/장고튜토리얼 (master)
$ pip install django

$ pip install djangorestframework
```

git에 연결하기   
```
USER@DESKTOP-MM3Q7OA MINGW64 ~/Desktop/장고튜토리얼/mysite
$ git init
Initialized empty Git repository in C:/Users/USER/Desktop/장고튜토리얼/mysite/.git/
(venv) (base) 
USER@DESKTOP-MM3Q7OA MINGW64 ~/Desktop/장고튜토리얼/mysite (master)
$ git add README.md
fatal: pathspec 'README.md' did not match any files
(venv) (base)
USER@DESKTOP-MM3Q7OA MINGW64 ~/Desktop/장고튜토리얼/mysite (master)
$ git remote add origin https://github.com/dltjdbs38/2023_Django_Mysite.git
(venv) (base)
USER@DESKTOP-MM3Q7OA MINGW64 ~/Desktop/장고튜토리얼/mysite (master)
$ git branch -M main
```
