from django.contrib import admin
from rooms.models import auditorium,conference,computerlab
# Register your models here.

admin.site.register(auditorium)
admin.site.register(conference)
admin.site.register(computerlab)
