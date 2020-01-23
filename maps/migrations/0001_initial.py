# Generated by Django 3.0.2 on 2020-01-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_json', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
    ]