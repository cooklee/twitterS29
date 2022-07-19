from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Tweet(models.Model):
    text = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} - {self.date.strftime('%Y %m %d %H:%M')}"