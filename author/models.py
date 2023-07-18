from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class CustomUser(AbstractUser):
    ROLES_CHOICES = (
        ('a','admin'),
        ('u','user')
    )

    roles = models.CharField(max_length=1,choices=ROLES_CHOICES)

class AuthorModel(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,default=None,null=True)
    category = models.ManyToManyField('category.CategoryModel')
    f_name = models.CharField(max_length=100,default='')
    l_name = models.CharField(max_length=100,default='')
    year_of_birth = models.DateField(default=datetime.now)
    year_of_death = models.DateField(default=datetime.now,null=True)
    birth_city_country = models.CharField(max_length=100,default='')
    died_city_country = models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='images/author')

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    class Meta:
        db_table = 'author'
