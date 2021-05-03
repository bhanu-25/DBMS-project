# Generated by Django 3.0.5 on 2021-04-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='crop_part',
            field=models.CharField(default='Whole plant', max_length=50),
        ),
        migrations.AddField(
            model_name='crop',
            name='disease_control',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='disease_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='disease_spread',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='disease_symptoms',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='crop_name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='disease',
        ),
    ]
