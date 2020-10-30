from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    twitter_link = models.CharField(max_length=100)



# будет подсчет количества лет автора
def count_age():
    pass
