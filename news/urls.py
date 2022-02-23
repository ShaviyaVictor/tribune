from django.urls import path
from . import views



urlpatterns = [

  path('', views.welcome, name='News~Welcome'),
  path('about/', views.about, name='News~About'),
  path('today/', views.news_of_day, name='News~Today'),
  path('results/', views.search_results, name='Search~Results'),
  
  # url path not working as expected
  path('archives/(\d{4}-\d{2}-\d{2})', views.past_days_news, name='News~Archives'),

]