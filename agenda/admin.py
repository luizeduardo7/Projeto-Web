from django.contrib import admin
from .models import Agenda
from barbearia.models import Barbeiro

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('usuario','barbeiro', 'servico', 'data', 'horario')  # Usando a função personalizada


admin.site.register(Agenda, AgendaAdmin)
