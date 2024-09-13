from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('check-view', views.checkView, name='checkView'),
    path('send', views.send, name='send')
]