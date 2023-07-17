from django.db import models
from datetime import datetime

class AuthorModel(models.Model):
    name = models.CharField(max_length=20,default='')
    fname = models.CharField(max_length=20,default='')
    date_of_birth = models.DateField(default=datetime.now)
    country = models.CharField(max_length=20,default='')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'author'
