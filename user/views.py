from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm


def register(request):
     if request.method == 'POST':
          user_form=UserRegistrationForm(request.POST)

          if user_form.is_valid():
               new_user = user_form.save(commit=False)
               new_user.set_password(user_form.cleaned_data['password'])
               new_user.save()
               profile = Profile.objects.create(user=new_user)
               messages.success(request, 'profile created successfully')
               return render(request, 'user/registration_done.html', {'new_user': new_user})
          else:
               messages.error(request, 'Error Registering your user')
     else:
          user_form = UserRegistrationForm()

     return render(request, 'registration/register.html', {'user_form': user_form})





@login_required()
def dashboard(request):
     return render(request, 'user/dashboard.html', {'section': 'dashboard'})


@login_required()
def edit(request):
     if request.method == 'POST':
          user_form = UserEditForm(instance=request.user, data=request.POST)
          profile_form = ProfileEditForm(instance=request.user, data=request.POST, files=request.FILES)
          if user_form.is_valid() and profile_form.is_valid():
               user_form.save()
               profile_form.save()
               messages.success(request, 'Profile updated successfully')
          else:
               messages.error(request, 'Error updating your profile')
     else:
          user_form = UserEditForm(instance=request.user)
          profile_form = ProfileEditForm(instance=request.user)
     return render(request, 'user/edit.html', {'user_form': user_form, 'profile_form': profile_form})
