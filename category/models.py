from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=65,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
