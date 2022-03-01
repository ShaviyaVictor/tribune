from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request) :

  if request.method == "POST" :
    form = UserRegisterForm(request.POST)

    if form.is_valid() :

      form.save()
      username = form.cleaned_data.get('username')

      messages.success(request, f'{ username }, your account has successfully been created!')

      return HttpResponseRedirect('login')

  else :
  
    form = UserRegisterForm()

  return render(request, 'users/register.html', { 'form':form })



# Types of messages
# messages.info
# messages.success
# messages.warning
# messages.error
# messages.debug


@login_required
def profile(request) :

  u_form = UserUpdateForm()
  p_form = ProfileUpdateForm()

  context = {
    'u_form': u_form,
    'p_form': p_form,
  }

  return render(request, 'users/profile.html', context)