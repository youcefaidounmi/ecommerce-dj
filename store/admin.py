from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="50"/>'.format(obj.image.url))
    list_display = ('title', 'price', 'image_tag', 'stock', 'is_available', 'category', 'created_date', 'modified_date')
    image_tag.short_description = 'image'
    prepopulated_fields = {'slug':('title',)}
admin.site.register(models.Product, ProductAdmin)
