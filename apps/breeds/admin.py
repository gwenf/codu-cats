from django.contrib import admin
from .models import Breed


class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'body_type', 'pattern')
    search_fields = ('name',)


admin.site.register(Breed, BreedAdmin)
