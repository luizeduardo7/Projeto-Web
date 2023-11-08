from django.contrib import admin
from .models import Agenda
from usuarios.models import Usuario

class AgendaAdmin(admin.ModelAdmin):
    list_display = ("usuario",)

admin.site.register(Agenda, AgendaAdmin)
