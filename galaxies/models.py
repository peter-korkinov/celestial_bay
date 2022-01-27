from django.db import models

from users.models import MyUser


class GalaxyModel(models.Model):
    name = models.CharField(max_length=30)
    constellation = models.CharField(max_length=30)
    name_origin = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    notes = models.CharField(max_length=300)
    image = models.URLField()
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __repr__(self):
        return f'{self.id} {self.name}'
