from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .logic import manejadorEventos_logic
from django.core import serializers
import json

from .models import Evento


@csrf_exempt
def evento_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            evento_dto = manejadorEventos_logic.create_evento(data)
            evento = serializers.serialize('json', [evento_dto, ])
            return HttpResponse(evento, 'application/json', status=201)

        except ValueError as ve:
            return JsonResponse({"error": str(ve)}, status=400)

#        except Exception as e:
#            return JsonResponse({"error": "Error interno del servidor"}, status=500)

    return JsonResponse({'error': 'No permitido'}, status=405)

@csrf_exempt
def eventos_por_paciente(request, ni_paciente):
    if request.method == 'GET':
        eventos = Evento.objects.filter(ni_paciente=ni_paciente)
        data = []
        for evento in eventos:
            data.append({
                'id': evento.id,
                'ni_paciente': evento.ni_paciente,
                'doctor_id': evento.doctor_id,
                'resultado': evento.resultado,
                'fecha': evento.fecha,
                'diagnostico': evento.diagnostico,
            })
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'No permitido'}, status=405)



