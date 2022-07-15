from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')


def page1(request):

    my_var = {
        'first_name':'Jeong',
        'last_name' : 'jihun',
        'some_list':[1,2,3],
        'some_dict':{'inside_dey' : 'inside_value'},
    }
    
    return render(request, 'my_app/page1.html', context=my_var)



def page2(request):
    return render(request, 'my_app/page2.html')

def page3(request):
    return render(request, 'my_app/page3.html')