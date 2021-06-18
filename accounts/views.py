
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import (
    RegistrationForm,
    EditProfileForm,
    UserProfileForm,
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method =='POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect (reverse('accounts:entry'))
    else:
      form = UserCreationForm()
    return render (request, 'accounts/signup.html', {'form':form})

def index(request):
    return render (request, "accounts/gis.html", {})


def entry(request):
    template = 'accounts/entry.html'
    context = {}
    return render (request, template, context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('/account')
            return redirect(reverse('home:register'))
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)
        
def view_profile(request, pk=None):
    args = {'user': request.user}
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args ={'user': user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect (reverse('accounts:view_profile')) #('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)

#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect(reverse('accounts:view_profile'))

#         else:
#             return redirect (reverse('accounts:change_password'))
#     else:
#         form = PasswordChangeForm(user=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/change_password.html', args)


    
def activate(request):
        form = UserProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            create = form.save()
            create.save
            
            return redirect('home:chat')
            
        args = {'form': form}
        return render(request, 'accounts/activate.html', args)
        
