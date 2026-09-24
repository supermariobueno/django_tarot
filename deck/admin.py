from symtable import Class

from django.contrib import admin
from .models import Deck

# Register your models here.

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'arcana_type')
    list_filter = ('arcana_type',)
    search_fields = ('name', 'number')
    
    