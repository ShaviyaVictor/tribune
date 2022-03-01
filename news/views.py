from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Editor, Article
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required





# Create your views here.
def welcome(request) :
  
  context = {
    'news': Editor.objects.all()
  }
  

  return render(request, 'news/home.html', context)


def about(request) :

  context = {
    'news': Editor.objects.all()
  }
  # title = 'News~Welcome'

  return render(request, 'news/about.html', context)

@login_required
def news_of_day(request) :

  date = dt.date.today()

  # A function that converts the date object to find the exact day
  day = convert_dates(date)

  html = f'''
      
            News for {day}, {date.day}-{date.month}-{date.year}
          
          '''

  news = Article.todays_news()
  
  return render(request, 'news/today.html', {'html': html, 'news':news})



def convert_dates(dates) :

  # A function that gets the weekday number fro the date
  
  day_number = dt.date.weekday(dates)
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  # Returning the actual day of the week
  day = days[day_number]

  return day



# Function to search for results
def search_results(request) :
  if 'article' in request.GET and request.GET['article'] :
    
    search_term = request.GET.get('article')
    

    context = {
    'found_articles' : Article.search_by_title(search_term),
    }
    messages = f'{ search_term }'

    return render(request, 'news/search.html', context, {'messages':messages})

  else :
    message = 'You haven\'t searched for any term!'

    return render(request, 'news/search.html', {'message':message})





#############################################
# Function not working
def past_days_news(request, past_date) :

  try :
  # Converts data from the string Url
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

  except ValueError :
  # Raise 404 error when ValueError is thrown
    raise Http404()
    
    assert False

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

  if date == dt.date.today() :
    return redirect(news_of_day)

  news = Article.days_news(date)

  return render(request, 'news/archive.html', {'date':date, "news":news})

#############################################


@login_required
def article(request) :
  
  try :
    article = Article.objects.all()

  except ObjectDoesNotExist :
    raise Http404()

  return render(request, 'news/article.html', { 'article':article })