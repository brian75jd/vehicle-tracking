from django.contrib import admin
from contact.models import *

@admin.register(SendMessage)
class AdminModel(admin.ModelAdmin):
    list_display = ('sender','content','email')
    search_fields = ('sender',)