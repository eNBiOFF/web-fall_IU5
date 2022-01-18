from django.db import models

# Create your models here.
class Film(models.Model):
    film_name = models.CharField(max_length=50, verbose_name="Название фильма")
    description = models.CharField(max_length=255, verbose_name="Цена акции")
    # is_growing = models.BooleanField(verbose_name="Растет ли акция в цене?")
    # date_modified = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз обновлялось значение акции?")
