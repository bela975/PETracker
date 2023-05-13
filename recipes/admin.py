from django.contrib import admin
from recipes.models import Event


from .models import Pet

# Register your models here.

admin.site.register(Event)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'breed', 'description', 'user']