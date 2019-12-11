from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<hero>', views.delete_hero, name='delete_hero'),
]
