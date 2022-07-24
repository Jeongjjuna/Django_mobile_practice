from django.shortcuts import render
from django.http import HttpResponse

def page1(request):
    return HttpResponse("page1")


def page1_datail(request, **kwargs):
    print(kwargs)
    print(kwargs[1])
    return HttpResponse(f"page1의 디테일 : ")


def page2(request):
    return HttpResponse("page2")


def page3(request):
    return HttpResponse("page3")


def page4(request):
    return HttpResponse("page4")
