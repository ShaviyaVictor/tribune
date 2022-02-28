from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.
def register(request) :

  if request.method == 'post' :
    form = UserCreationForm(request.post)

    if form.is_valid() :
      username = form.cleaned_data.get('username')

      messages.success(request, f'{ username }, your account has successfully been created!')

      return redirect('Article')

  else :
  
    form = UserCreationForm()

  return render(request, 'users/register.html', { 'form':form })



# Types of messages
# messages.info
# messages.success
# messages.warning
# messages.error
# messages.debug