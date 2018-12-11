from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
##    path('predict/verdict.html',views.verdict, name='verdict'),
]
