from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home,name='home'),
    path('home', views.home,name='home'),
    path('service', views.service,name='service'),
    path('contact', views.contact,name='contact'),
    path('support', views.support,name='support'),
    path('login', views.loginuser,name='login'),
    path('logout', views.logoutuser,name='logout'),
]
