from turtle import title
from django.test import TestCase
from .models import Article, Tag, Editor



# Create your tests here.
class EditorTestClass(TestCase) :
  
  #set up method
  def setUp(self) :
    self.josphine = Editor(first_name='Josphine', last_name ='Mbaisi', email ='mbaisijosphine@gmail.com')

  # testing the instance
  def test_instance(self) :
    self.assertTrue(isinstance(self.josphine, Editor))

  # Testing the Save method
  def test_save_method(self) :
    self.josphine.save_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors) > 0)

  # Testing the delete method || Must fail coz the editor object is not supposed to be deleted
  # def test_delete_method(self) :
  #   self.josphine.delete_editor()
  #   editors = Editor.objects.all()
  #   self.assertTrue(len(editors) < 1)  


class TagTestClass(TestCase) :

  # set up method
  def setUp(self) :
    self.top = Tag(id='1')

  # Testing the instance
  def test_instance(self) :
    self.assertTrue(isinstance(self.top, Tag))

  # Testing the save_method for the Tag model
  def test_save_method(self) :
    self.top.save_tag()
    tags = Tag.objects.all()
    self.assertTrue(len(tags) > 0)

  # Testing the delete method 
  def test_delete_method(self) :
    self.top.delete_editor()
    tags = Tag.objects.all()
    self.assertTrue(len(tags) -+1)


class ArticleTestClass(TestCase) :
  
  def setUp(self) :

    # Creating a new editor and saving it
    self.josphine = Editor(first_name='Josphine', last_name ='Mbaisi', email ='mbaisijosphine@gmail.com')

    self.josphine.save_editor()


    # Creating a new tag and saving it
    self.new_tag = Tag(name = '#testing')

    self.new_tag.save()


    # Creating a new article and saving it
    self.new_article = Article(title='Test Article', post='This is a random test post', editor='self.josphine')

    self.new_article.save()

    self.new_article.tags.add(self.new_tag)


  def test_news_of_day(self) :
    today_news = Article.todays_news()
    
    self.assertTrue(len(today_news) > 0)


  # Craeting a delete method that deletes all instances of our models from the database after each test.

  def tearDown(self) :
    Editor.objects.all().delete()
    Tag.objects.all().delete()
    Article.objects.all().delete()





  