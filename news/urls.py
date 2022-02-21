from django.urls import path
from . import views



urlpatterns = [

  path('', views.welcome, name='News~Welcome'),
  path('about/', views.about, name='News~About'),
  path('today/', views.news_of_day, name='News~Today'),

]