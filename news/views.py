from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt



# Create your views here.
def welcome(request) :
  
  return HttpResponse('<h1>Welcome to the Moringa Tribune</h1>')


def about(request) :

  return HttpResponse('<h1>About Page for Moringa Tribune</h1>')


def news_of_day(request) :

  date = dt.date.today()
  html = f'''
      <html>
        <body>
          <h1>
            {date.day}-{date.month}-{date.year}
          </h1>
        </body>
      </html>
          '''
  
  return HttpResponse(html)