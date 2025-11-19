from django.urls import path
from . import views

app_name = "inquiry"

urlpatterns = [
    #  どんなパス, 動かす関数, このパスの名前
    path('', views.index, name='index'),
    path('article/list', views.list, name='list'),
]