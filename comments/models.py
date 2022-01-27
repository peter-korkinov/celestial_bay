from django.db import models

from users.models import MyUser
from posts.models import PostModel


class CommentsModel(models.Model):
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    # to do likes functionality maybe

    def __repr__(self):
        return f'comment {self.id} by {self.creator.id} {self.creator.email}'
