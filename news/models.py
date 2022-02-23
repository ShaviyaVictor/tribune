from django.utils import timezone
from django.db import models 
import datetime as dt



# Create your models here.
class Editor(models.Model) :
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()
  phone_number = models.CharField(max_length=10, blank=True)


  def __str__(self) :
      return self.first_name

  class Meta :
    ordering = ['-first_name']

  # Define save_editor() method to pass the test
  def save_editor(self) :
    self.save()

  # # Define the delete_editor() method to pass the test by raising an error
  # def delete_editor(self) :
  #   self.delete()


class Tag(models.Model) :
  name = models.CharField(max_length=30)

  
  def __str__(self) -> str:
      return self.name

  class Meta :
    ordering = ['-name']

  def save_tag(self) :
    self.save()

  # Define the delete_editor() method 
  def delete_editor(self) :
    self.delete()


class Article(models.Model) :
  title = models.CharField(max_length=60)
  post = models.TextField()
  # foreign key column that will store the ID of the Editor from the Editor table.
  editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
  # ManyToManyField field that creates a separate join table. This new table handles mapping between articles and tags.
  tags = models.ManyToManyField(Tag)
  # add a timestamp to our model and use an argument to enable us edit the time of edit
  pub_date = models.DateTimeField(default=timezone.now)



  def __str__(self) -> str:
      return self.title

  class Meta :
    ordering = ['-title']

  @classmethod
  def todays_news(cls) :
    today = dt.date.today()
    news = cls.objects.filter(pub_date__date = today)

    return news

  @classmethod
  def days_news(cls, date) :
    news = cls.objects.filter(pub_date__date = date)

    return news

  @classmethod
  def search_by_title(cls, search_term) :
    news = cls.objects.filter(title__icontains = search_term)

    return news