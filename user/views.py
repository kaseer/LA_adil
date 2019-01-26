from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm


def register(request):
     if request.method == 'POST':
          user_form=UserRegistrationForm(request.POST)

          if user_form.is_valid():
               new_user = user_form.save(commit=False)
               new_user.set_password(user_form.cleaned_data['password'])
               profile = Profile.objects.create(user=new_user)
               new_user.save()
               return render(request, 'user/registration_done.html', {'new_user': new_user})
     else:
          user_form = UserRegistrationForm()

     return render(request, 'registration/register.html', {'user_form': user_form})





@login_required()
def dashboard(request):
     return render(request, 'user/dashboard.html', {'section': 'dashboard'})
