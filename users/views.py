from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,TemplateView,FormView,RedirectView
from . import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from users.forms import UserSignUpForm
from django.core.exceptions import ValidationError
from django.utils.http import is_safe_url
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
# Create your views here.

class UserCreateView(CreateView):
    fields = ('first_name','last_name','email','mobile','password','password2')
    model = models.User
    template_name = 'users/register.html'

    def get_success_url(self):
            return reverse('users:success')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        form.fields['password2'].widget = forms.PasswordInput()
        return form

    def form_valid(self,form):
      password = form.cleaned_data.get('password')
      password2 = form.cleaned_data.get('password2')
      if not password == password2:
        form.add_error('password2', 'Passwords must match')
        return super(UserCreateView, self).form_invalid(form)
      return super(UserCreateView,self).form_valid(form)


class successView(TemplateView):
    template_name = 'users/base.html'


class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/account/register/'
    template_name='users/login.html'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('users:success')


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
