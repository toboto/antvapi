# Generated by Django 3.0.2 on 2020-01-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoarea',
            name='area',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='geoarea',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='geoarea',
            name='prefix',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
