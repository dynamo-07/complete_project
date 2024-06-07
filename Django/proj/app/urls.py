from django.urls import path
from .views import *
urlpatterns = [
    path('home/',index,name='home'),
    path('mens/',mens,name='mens'),
    path('', loginpage, name='login'),
    path('womens/',womens,name='womens'),
    path('children/',childrens,name='children'),
    path('', loginpage, name='login'),
    path('login/', loginpage, name='login'),
    path('main/', main123, name='home'),
]