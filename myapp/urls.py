from django.urls import path
from . import views

urlpatterns = [
    #이경로로 들어왔을 시 views.py의 func_1함수 실행
    path('index/', views.index, name='index'), 

    path('detail/', views.detail, name='detail'),
    
    path('results/<topic>/', views.results, name='results'),
    
    path('vote/<topic>/', views.vote, name='vote'),

]




'''----------------------------------------'''

# {% url 'name_1' %} 나중에사용가능