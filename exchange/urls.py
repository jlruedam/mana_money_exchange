from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.calculate, name='calculate'),
    path('tv-view/', views.tv_view, name='tv_view'),
    path('divisas/', views.divisa_list, name='divisa_list'),
    path('divisas/new/', views.divisa_create, name='divisa_create'),
    path('divisas/<int:pk>/edit/', views.divisa_edit, name='divisa_edit'),
    path('flags/proxy/<str:flag_code>.png', views.flag_proxy, name='flag_proxy'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]