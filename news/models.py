from django.utils import timezone
from django.db import models 



# Create your models here.
class Editor(models.Model) :
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()


  def __str__(self) :
      return self.first_name

  class Meta :
    ordering = ['-first_name']

  # Define save_editor() method to pass the test
  def save_editor(self) :
    self.save()

  # Define the delete_editor() method to pass the test
  def delete_editor(self) :
    self.delete()


class Tag(models.Model) :
  name = models.CharField(max_length=30)

  
  def __str__(self) -> str:
      return self.name

  class Meta :
    ordering = ['-name']


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