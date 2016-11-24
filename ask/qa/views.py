from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from .models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

@require_GET
def index(requst, page):
    questions = Question.new()
    # context = {'questions': questions}
    paginator, page, limit = paginate(request, question)
    context = {'questions': page, 'paginator': paginator, 'limit': limit}
    return render(request, 'index.html', context)

@require_GET
def popular(request, page):
    questions = Question.popular()
    # context = {'questions': questions}
    paginator, page, limit = paginate(request, question)
    context = {'questions': page, 'paginator': paginator, 'limit': limit}  
    return render(request, 'popular.html', context)

def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = q.answer_set.all()
    context = {'question': question, 'answers': answers}
    return render(request, 'question.html', context)

def paginate(requst, params):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        raise Http404
    
    try:
        page = paginator.page(paginator.num_pages)

    return paginator, page, limit