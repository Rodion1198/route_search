from django.contrib import admin

from .models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ['name', 'from_city', 'to_city', 'travel_time']

    class Meta:
        model = Train
