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

  # A function that converts the date object to find the exact day
  day = convert_dates(date)

  html = f'''
      <html>
        <body>
          <h1>
            News for {day}, {date.day}-{date.month}-{date.year}
          </h1>
        </body>
      </html>
          '''
  
  return HttpResponse(html)


def convert_dates(dates) :

  # A function that gets the weekday number fro the date
  
  day_number = dt.date.weekday(dates)
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  # Returning the actual day of the week
  day = days[day_number]

  return day