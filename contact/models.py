from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# First_name (string), last_name (string), phone (string),
# email (email), created_date (data), description (text)
# category (foreign key), show (boolean), picture (imagem)

# Depois
# owner (foreign key)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=30)

    def __str__(self) -> str:
       return self.name
   
   
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='picutures/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 blank=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 blank=True)
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
