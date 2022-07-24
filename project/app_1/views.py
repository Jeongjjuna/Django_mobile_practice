from django.shortcuts import render
from django.http import HttpResponse

def page1(request):
    #
    return render(request, 'app_1/page1.html')


def page1_datail(request, **kwargs):
    print(kwargs)
    return render("page1_detaie")


def page2(request):
    return HttpResponse("page2")


def page3(request):
    return HttpResponse("page3")


def page4(request):
    return HttpResponse("page4")
