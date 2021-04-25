# Generated by Django 3.2 on 2021-04-25 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='number of train')),
                ('travel_time', models.PositiveSmallIntegerField(verbose_name='travel time')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city_set', to='cities.city', verbose_name='from city')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_set', to='cities.city', verbose_name='In city')),
            ],
            options={
                'verbose_name': 'Train',
                'verbose_name_plural': 'Trains',
                'ordering': ['travel_time'],
            },
        ),
    ]