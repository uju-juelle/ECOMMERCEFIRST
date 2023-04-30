from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Category, Product, subscribers])

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "subject", "message"]

admin.site.register(Contact, ContactAdmin)