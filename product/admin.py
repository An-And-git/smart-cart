from django.contrib import admin
from .models import Products

admin.site.site_header = 'Smart Cart Admin'


class SmartcartAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)


admin.site.register(Products, SmartcartAdmin)
