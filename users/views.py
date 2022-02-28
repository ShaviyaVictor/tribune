from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def register(request) :

  if request.method == 'post' :
    form = UserCreationForm(request.post)

    if form.is_valid() :
      username = form.cleaned_data.get('username')

  else :
  
    form = UserCreationForm()

  return render(request, 'users/register.html', { 'form':form })
