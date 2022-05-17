from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:news_link>/', views.detail, name='news_detail'),
    path('create/', views.create_news, name='create_news'),
]
