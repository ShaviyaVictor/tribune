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

  