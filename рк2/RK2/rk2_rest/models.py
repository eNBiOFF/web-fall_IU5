from django.db import models

# Create your models here.
class Musicians(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Имя")
    role = models.CharField(max_length=32, verbose_name="Роль в оркестре")
    id_orkestry = models.ForeignKey('Orchestrys', models.DO_NOTHING, db_column="id_orkestry", blank=True, null=False)

    class Meta:
        db_table = 'musician'

class Orchestrys(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="Название оркестра")

    class Meta:
        db_table = 'orchestry'
