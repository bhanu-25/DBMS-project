# Generated by Django 3.0.5 on 2021-04-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210414_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='date published'),
        ),
    ]
