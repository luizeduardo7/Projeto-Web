from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Barbeiro)
admin.site.register(Servico)
admin.site.register(Agenda)
