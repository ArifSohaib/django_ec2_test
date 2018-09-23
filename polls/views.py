from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.
def index(request):
    return HttpResponse("Hello world, you are at the polls index")

def detail(request, question_id):
    return HttpResponse("You're looking at question {}: {}".format(question_id, Question.objects.get(pk=question_id)))

def results(request, question_id):
    return HttpResponse("You're looking at results of question {}".format(question_id))

def vote(request, question_id):
    q =  Question.objects.get(pk=question_id)
    res = "You're voting on question {}: {}".format(question_id,q)
    c = Choice.objects.filter(question_id=question_id)
    for i in c:
        res += "<br>{}".format(i)
    return HttpResponse(res)