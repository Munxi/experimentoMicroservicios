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
            
            #doctor
            doctor_resp = requests.get(f"{settings.DOCTORES_MS_URL}/{data['doctorEncargado']}")
            if doctor_resp.status_code != 200:
                return JsonResponse({"error": "El doctor no existe"}, status=400)

            evento_dto = manejadorEventos_logic.create_evento(data)
            evento = serializers.serialize('json', [evento_dto, ])
            return HttpResponse(evento, 'application/json', status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)