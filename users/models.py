from email.policy import default
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model) :
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  city = models.CharField(max_length=30)
  bio = models.CharField(max_length=200)


  def __str__(self) -> str:
      return self.user

  class Meta :
    ordering = ['-user']
