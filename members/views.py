from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
#from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
#from virtualbookshelf2022.models import Profile


class UserRegisterView(generic.CreateView):
    #form_class = SignUpForm
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

