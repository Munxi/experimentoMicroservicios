from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .logic import informacionPaciente_logic as pl
from django.core import serializers

@csrf_exempt
def paciente_view(request):
    if request.method == 'GET':
        id = request.GET.get("NI", None)
        if id:
            paciente_dto = pl.get_paciente(id)
            paciente = serializers.serialize('json', [paciente_dto])
            eventos = [paciente]
            for evento_dto in eventos_dto:
                eventos.append(serializers.serialize('json', [evento_dto]))
            return HttpResponse(eventos, 'application/json')
    if request.method == 'POST':
        paciente_dto = pl.create_paciente(json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto, ])
        return HttpResponse(paciente, 'application/json')
