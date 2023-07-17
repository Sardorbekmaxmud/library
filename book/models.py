from django.db import models
from datetime import datetime

# Create your models here.
class BookModel(models.Model):
    user = models.ForeignKey('author.CustomUser',on_delete=models.SET_NULL,default=None,null=True)
    category = models.ForeignKey('category.CategoryModel',on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey('author.AuthorModel',on_delete=models.SET_NULL,default=None,null=True)
    name = models.CharField(max_length=200,default='')
    about = models.TextField(default='')
    year = models.DateField(default=datetime.now)
    page = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to="images/book")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'