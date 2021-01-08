from django.urls import path
from rooms import views

app_name='rooms'

urlpatterns =[
  path('auditorium/',views.AuditoriumView.as_view(),name='auditorium'),
  path('conference/',views.ConferenceView.as_view(),name='conference'),
  path('computerlab/',views.ComputerlabView.as_view(),name='computerlab'),
]
