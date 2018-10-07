from django.urls import path

from . import views

urlpatterns = [
    path('', views.ex02_form, name='ex02'),
]
