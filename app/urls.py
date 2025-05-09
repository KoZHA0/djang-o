from django.urls import path
from . import views

urlpatterns =[

    path ('', views.home, name='home'),
    path ('about/', views.about, name='about'),
    path ('django/', views.django, name='django'),
    path ('python/', views.python, name='python'),
    path ('mvt/', views.mvt, name='mvt'),

]
