from django.urls import path

from . import views

urlpatterns = [
    path('', views.bics, name='bics'),
]
