from django.db import models
from author.models import AuthorModel


class BookCategoryModel(models.Model):
    name = models.CharField(max_length=65,default='')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'book_category'

class BookModel(models.Model):
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,default='')
    category = models.ForeignKey(BookCategoryModel,on_delete=models.SET_NULL,null=True)
    page = models.PositiveSmallIntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'book'
