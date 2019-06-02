from django.urls import path

from sonder.scheduler import views

urlpatterns = [
    path('', views.home, name='home'),
]