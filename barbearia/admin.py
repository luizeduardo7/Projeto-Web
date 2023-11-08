from django.contrib import admin
from .models import *

class BarbeiroAdmin(admin.ModelAdmin):
    list_display = ("nome",)

class ServicoAdmin(admin.ModelAdmin):
    list_display = ("titulo","preco")

admin.site.register(Barbeiro,BarbeiroAdmin)
admin.site.register(Servico,ServicoAdmin)

