from django.db import models

from users.models import MyUser


class PostModel(models.Model):
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    picture = models.URLField(max_length=500, blank=True)
    # to do likes functionality maybe

    def __repr__(self):
        return f'{self.id} {self.title} by {self.creator.id} {self.creator.email}'
