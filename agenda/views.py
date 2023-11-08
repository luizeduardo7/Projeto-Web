from django.http import HttpResponse
from django.template import loader
from barbearia.models import Barbeiro

def agendamento(request):
    barbeiros = Barbeiro.objects.all().values()
    template = loader.get_template('agendamento.html')
    context = {
        'barbeiros': barbeiros,
    }
    return HttpResponse(template.render(context, request))
    
