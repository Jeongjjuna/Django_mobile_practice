from django.shortcuts import render
from .models import My_program_language
from .forms import PostForm

def page1(request):
    my_program_language = My_program_language.objects.all()
    context = {"My_program_language" : my_program_language}
    return render(request, 'app_1/page1.html', context = context)


def page1_datail(request, **kwargs):
    print(kwargs)
    return render("page1_detaie")


def page2(request):
    post_form = PostForm()
    return render(request, 'app_1/page2.html', {'form' : post_form})


def page3(request):
    return render("page1_detaie")


def page4(request):
    return render("page1_detaie")
