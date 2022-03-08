from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

  path('', views.welcome, name='News~Welcome'),
  path('about/', views.about, name='News~About'),
  path('today/', views.news_of_day, name='News~Today'),
  path('results/', views.search_results, name='Search~Results'),
  path('article/', views.article, name='Article'),
  path('ajax/newsletter', views.newsletter, name='newsletter')
  
  # url path not working as expected
  path('archives/(\d{4}-\d{2}-\d{2})', views.past_days_news, name='News~Archives'),

]

# if settings.DEBUG :
#   urlpatterns += static(settings.MEDIA_URL)

  # , document_root = settings.MEDIA_ROOT