from django.db import models
from users.models import User
from rooms.models import auditorium,conference,computerlab
import uuid
# Create your models here.

class BookAuditorium(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    room_id=models.ForeignKey(auditorium,on_delete=models.CASCADE)
    booking_id=models.UUIDField(primary_key = True,default = uuid.uuid4,
                                editable = False)
    book_from=models.DateTimeField()
    book_till=models.DateTimeField()

class BookConference(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    room_id=models.ForeignKey(conference,on_delete=models.CASCADE)
    booking_id=models.UUIDField(primary_key = True,default = uuid.uuid4,
                                editable = False)
    book_from=models.DateTimeField()
    book_till=models.DateTimeField()


class BookComputerlab(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    room_id=models.ForeignKey(computerlab,on_delete=models.CASCADE)
    booking_id=models.UUIDField(primary_key = True,default = uuid.uuid4,
                                editable = False)
    book_from=models.DateTimeField()
    book_till=models.DateTimeField()
