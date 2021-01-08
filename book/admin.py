from django.contrib import admin
from book.models import BookAuditorium,BookConference,BookComputerlab

# Register your models here.

admin.site.register(BookAuditorium),
admin.site.register(BookConference),
admin.site.register(BookComputerlab),
