from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class home(TemplateView):
    template_name='index.html'

class AuditoriumView(TemplateView):
    template_name='rooms/auditorium.html'

class ConferenceView(TemplateView):
    template_name='rooms/conference.html'

class ComputerlabView(TemplateView):
    template_name='rooms/computer_lab.html'
