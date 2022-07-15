from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(f'여기는 index사이트')
    #return render(request, 'pages/1.html')


def detail(request):
    return HttpResponse(f'여기는 detail사이트')
    #return render(request, 'pages/1.html', question_id)


def results(request, topic):
    return HttpResponse(f'여기는 results사이트 {topic} 번')
    #return render(request, 'pages/1.html', question_id)


def vote(request, topic):
    return HttpResponse(f'여기는 vote사이트 {topic} 번')
    #return render(request, 'pages/1.html', question_id)

