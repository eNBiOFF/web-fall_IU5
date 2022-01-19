from django.db import models

# Create your models here.
class Filem(models.Model):
    film_name = models.CharField(max_length=50, verbose_name="название фильма")
    description = models.CharField(max_length=255, verbose_name="описание фильма")