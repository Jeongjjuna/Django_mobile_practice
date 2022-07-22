from django.urls import path

from . import views

urlpatterns = [
    path('page1', views.page1, name='page1'),
    path('page1/<id>/<name>/<age>', views.page1_datail, name='page1_datail'),

    path('page2', views.page2, name='page2'),

    path('page3', views.page3, name='page3'),

    path('page4', views.page4, name='page4')
]