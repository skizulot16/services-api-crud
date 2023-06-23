# Generated by Django 4.2.2 on 2023-06-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('time', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=27)),
                ('price', models.FloatField(default=0.0)),
                ('discount', models.IntegerField(default=0)),
            ],
        ),
    ]
