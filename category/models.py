from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=65,default='')

    def __str__(self):
        return self.name

    class Meta:
<<<<<<< HEAD
        db_table = 'category'
=======
        db_table = 'category'
>>>>>>> d7caeb229884e831d99fd1917b634cdd7a31c8f1
