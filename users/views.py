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

  if request.method == "POST" :

    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(
      request.POST, 
    request.FILES, 
    instance=request.user.profile
    )

    if u_form.is_valid() and p_form.is_valid() :
      u_form.save()
      p_form.save()

      username = u_form.cleaned_data.get('username')
      messages.success(request, f'{ username }, your account has successfully been updated!')

      return HttpResponseRedirect('profile')

  else :
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'u_form': u_form,
    'p_form': p_form,
  }

  return render(request, 'users/profile.html', context)