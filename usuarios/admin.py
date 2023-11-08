from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")

admin.site.register(Usuario, UsuarioAdmin)
