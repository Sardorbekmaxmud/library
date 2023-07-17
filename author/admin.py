from django.contrib import admin
from .models import CustomUser,AuthorModel

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AuthorModel)
