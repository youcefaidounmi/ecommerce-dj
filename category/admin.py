from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" />'.format(obj.image.url))

    list_display = ('title', 'image_tag')
    image_tag.short_description = 'image'
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(models.Category, categoryAdmin)
