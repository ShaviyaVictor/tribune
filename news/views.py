from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt



news = [

  {
    'author': 'Victor Shaviya',
    'title': 'Templating in Django',
    'content': 'Templating can be very time saving and efficient',
    'date_posted': '21st of February 2022'
  },

  {
    'author': 'Hycine Mapendo',
    'title': 'Templating in Flask',
    'content': 'Templating here was also time saving and efficient',
    'date_posted': '15th of January 2022'
  }

]



# Create your views here.
def welcome(request) :
  
  reports = {
    'news': news
  }
  

  return render(request, 'news/home.html', reports)


def about(request) :

  reports = {
    'news': news
  }
  # title = 'News~Welcome'

  return render(request, 'news/about.html', reports)


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
  
  return render(request, 'news/today.html')


def convert_dates(dates) :

  # A function that gets the weekday number fro the date
  
  day_number = dt.date.weekday(dates)
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  # Returning the actual day of the week
  day = days[day_number]

  return day


# Function not working
def past_days_news(request, past_date) :

  try :
  # Converts data from the string Url
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

  except ValueError :
  # Raise 404 error when ValueError is thrown
    raise Http404()

  day= convert_dates(date)

  html = f'''
      <html>
        <body>
          <h1>
            News for {day}, {date.day}-{date.month}-{date.year}
          </h1>
        </body>
      </html>
          '''

  return render(request, 'news/archive.html')