from django.urls import path
from . import views

#アプリの名前　これはお問い合わせフォームアプリ
app_name = "inquiry"

#お問い合わせフォームアプリに使う関数とパスのリスト
urlpatterns = [
    #  どんなパス, 動かす関数, このパスの名前
    path('', views.index, name='index'),
    path('', views.list, name='list'),
]