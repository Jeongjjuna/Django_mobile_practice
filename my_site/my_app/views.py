from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')

def page1(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/page1.html')

def page2(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/page2.html')

def page3(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/page3.html')