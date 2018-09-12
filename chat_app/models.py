from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

status1 = (
    ('on', 'on'),
    ('off', 'off')
)


class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    #handle = models.TextField()
    userId = models.TextField(blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        # return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())
        return ' {message}'.format(**self.as_dict())

    # @property
    # def formatted_timestamp(self):
    #     return self.timestamp.strftime('%b %-d %-I:%M %p')
    #

    def as_dict(self):
        # return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}
        return {'message': self.message }


#일대일 채팅방 model
class Oneroom(models.Model):
    users = models.ManyToManyField(User, related_name='checking')
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=status1, default='on')

    def __str__(self):
        roomuser = ", ".join(str(name) for name in self.users.all())
        return "{}".format(roomuser)


class Onemessage(models.Model):
    room = models.ForeignKey(Oneroom, related_name='onemessages', on_delete=models.CASCADE)
    userId = models.TextField(blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return ' {message}'.format(**self.as_dict())

    def as_dict(self):
        # return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}
        return {'message': self.message }

