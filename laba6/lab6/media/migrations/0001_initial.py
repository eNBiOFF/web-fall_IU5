# Generated by Django 4.0.1 on 2022-01-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_name', models.CharField(max_length=50, verbose_name='название фильма')),
                ('description', models.CharField(max_length=255, verbose_name='описание фильма')),
            ],
        ),
    ]
