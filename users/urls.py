from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
   path('register/',views.UserCreateView.as_view(),name='register'),
   path('login/',views.LoginView.as_view(),name='login'),
   path('success/',views.successView.as_view(),name='success')
  # path('login/',views.user_login,name='user_login'),
]
