from django.http import HttpResponse
from django.template import loader

def teste(request):
    template = loader.get_template('paginateste.html')
    return HttpResponse(template.render())

def cadastro(request):
    return HttpResponse("Olá Mundo! - Portal Biblioteca")