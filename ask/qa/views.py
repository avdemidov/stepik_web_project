from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET
from .models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

@require_GET
def index(request, *args, **kwargs):
    questions = Question.objects.new()
    # context = {'questions': questions}
    paginator, page, limit = paginate(request, questions)
    context = {'questions': page, 'paginator': paginator, 'limit': limit}
    return render(request, 'index.html', context)

@require_GET
def popular(request, *args, **kwargs):
    questions = Question.objects.popular()
    # context = {'questions': questions}
    paginator, page, limit = paginate(request, questions)
    context = {'questions': page, 'paginator': paginator, 'limit': limit}  
    return render(request, 'popular.html', context)

def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = q.answer_set.all()
    context = {'question': question, 'answers': answers}
    return render(request, 'question.html', context)

def paginate(request, params):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    paginator = Paginator(params, limit)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    try:
        page = paginator.page(paginator.num_pages)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page, limit
