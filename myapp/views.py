from django.shortcuts import render

def func_1(request):
    aaa = {'a': 456, 'b': 789}
    return render(request, 'pages/1.html', aaa) #1.html페이지로 aaa딕셔너리 넘겨버림
