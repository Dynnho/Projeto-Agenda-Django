from django.db import models
from django.utils import timezone

# id (primary key - automático)
# First_name (string), last_name (string), phone (string),
# email (email), created_date (data), description (text)
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
