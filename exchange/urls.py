from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tv-view/', views.tv_view, name='tv_view'),
    path('calculate/', views.calculate, name='calculate'),
]