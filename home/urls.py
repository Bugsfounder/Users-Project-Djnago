from django import views
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
