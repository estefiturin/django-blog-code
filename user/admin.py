from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username','password')}),
        ('Informacion Personal', {'fields': ('first_name', 'last_name')}),
        ('Otros', {'fields':('is_active', ) }),
        #propiedad creada en models
        ('Redes Sociales', {'fields': ('web_site', 'twitter')}),
    )
    