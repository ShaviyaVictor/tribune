from django.urls import path
from . import views



urlpatterns = [

  path('', views.welcome, name='News~Welcome'),
  path('about/', views.about, name='News~About'),

]