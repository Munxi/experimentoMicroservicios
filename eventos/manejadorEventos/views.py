from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .logic import manejadorEventos_logic
from django.core import serializers
import json
import requests
from django.conf import settings

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

        except Exception as e:
            return JsonResponse({"error": "Error interno del servidor"}, status=500)

    return JsonResponse({'error': 'No permitido'}, status=405)
