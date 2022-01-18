from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=30)
    desription = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'films'