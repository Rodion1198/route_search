# Generated by Django 3.2 on 2021-04-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0002_alter_train_options'),
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='trains',
            field=models.ManyToManyField(to='trains.Train', verbose_name='Through cities'),
        ),
    ]
