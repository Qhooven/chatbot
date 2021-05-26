from django.db import models

#Message model to be displayed by bot
class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    author = models.TextField()