from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .logic import manejadorEventos_logic as el
from django.core import serializers

@csrf_exempt
def evento_view(request):
    if request.method == 'POST':
        evento_dto = el.create_evento(json.loads(request.body))
        evento = serializers.serialize('json', [evento_dto, ])
        return HttpResponse(evento, 'application/json')