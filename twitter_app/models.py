from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    #my_groups


class Tweet(models.Model):
    text = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} {self.author.username}"


class Group(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='my_groups')
    users = models.ManyToManyField(User)