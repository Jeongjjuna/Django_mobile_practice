from django.urls import path
from myapp import views

urlpatterns = [
    #이경로로 들어왔을 시 views.py의 func_1함수 실행
    path('', views.func_1, name='name_1'), # {% url 'name_1' %} 나중에사용가능
    #path('create/', views.create),
    #path('read/<id>/', views.read) #<id>는 언제든지 아무값이 나 들어올 수있다는 뜻
]