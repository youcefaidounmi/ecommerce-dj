from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name','last_name', 'is_superadmin', 'is_admin','is_staff','is_active', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)


admin.site.register(models.Account, AccountAdmin)
