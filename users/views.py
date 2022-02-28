from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.
def register(request) :

  if request.method == "POST" :
    form = UserCreationForm(request.POST)

    if form.is_valid() :
      username = form.cleaned_data.get('username')

      messages.success(request, f'{ username }, your account has successfully been created!')

      return HttpResponseRedirect('Article')

  else :
  
    form = UserCreationForm()

  return render(request, 'users/register.html', { 'form':form })



# Types of messages
# messages.info
# messages.success
# messages.warning
# messages.error
# messages.debug