# from django.http import HttpResponse # 추가
from django.shortcuts import render, get_object_or_404, redirect # render : template에게 컨텐츠를 전달하는 함수. template : 사용자에게 보여주기 위해 html
from pybo.models import Question # , Answer
from django.utils import timezone
from pybo.forms import QuestionForm # forms.py에서 Class import 

### views.py는 client와 template의 중간자 역할. 데이터를 넘겨주고, 정의하는 부분

# 우리는 오늘 DB와 연동한 template를 사용자에게 보여줄 것이다.
def index(request): # 사용자로부터 인자를 받자(요청 = request)
    question_list = Question.objects.order_by('-create_date') # DB의 objects를 가져와서 시간순 정렬
    # order_by default는 내림차순, 우리는 최근부터 보여줘야하니까 오름차순으로 -
    context = {'question_list' : question_list} # dict로 포장해서 사용자에게 보내주기
    return render(request, 'pybo/question_list.html', context) # 요청, template 경로, 넘겨줄내용

# 질문 pybo/1 , pybo/2 에 들어갈 때 보여줄 함수 정의
def detail(req, q_id): # 아까 urls.py에서 만든 <int:q_id> 를 detail 이 알아야한다.
    # q = Question.objects.get(id=q_id)
    q = get_object_or_404(Question, pk=q_id)
    # primary key가 있는 q_id면 
    # 없는 q_id 를 요청하면 (ex 29249) 404 띄워주기 
    context = {'question' : q, 'request': req } # dictionary로 프론트단에 넘겨줄 데이터 포장
    # context = <WSGIRequest: GET '/pybo/3/'> 장고로 만들어진 사이트 있나요?
    return render(req, 'pybo/question_detail.html', context) # 요청, 템플릿을 누가받을건지, 넘겨줄내용

# 각 질문 pybo/2에 대한 질문 답변 POST 하기
def answer_create(req,q_id):
    ## sol1.
    q = get_object_or_404(Question, pk= q_id)
    q.answer_set.create(content= req.POST.get('content'),
                        create_date = timezone.now()) # 포스트 방식 요청
    # -> create : ORM 사용해 Answer 테이블에 새로운 row 추가.
    ## sol2. from pybo.models import Answer 를 해야함
    # a = Answer(question = q, content= req.POST.get('content'), create_date = timezone.now())
    # a.save()
    return redirect('pybo:detail', q_id = q.id) # pybo에 detail 함수에다가 

def question_create(req):
    print(req)
    if req.method == "POST":
        form = QuestionForm(req.POST)
        if form.is_valid(): # 만약 form에 데이터가 있으면
            q = form.save(commit=False) # ORM / commit=False 는 임시저장
            q.create_date = timezone.now()
            q.save()
    else: # POST가 아니면 단순 페이지 보여주기만. 
        form = QuestionForm()
    return render(req, 'pybo/question_form.html', {'form': form})