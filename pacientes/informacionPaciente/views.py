from django.http import JsonResponse
from pymongo import MongoClient
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId

@api_view(['GET', 'POST'])
def paciente_view(request, id=None):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    pacientes = db['pacientes']
    pacientesCriticos = db['pacientesCriticos']
    if request.method == 'GET':
        dto = pacientesCriticos.find_one({'NI': id})
        if dto is None:
            dto = pacientes.find_one({'NI': id})
        jsonData = {
            'id': str(dto['_id']),
            'nombres': dto['nombres'],
            'apellidos': dto['apellidos'],
            'NI': dto['NI'],
            'sexo': dto['sexo'],
            'eps': dto['eps'],
        }
        client.close()
        return JsonResponse(jsonData, content_type='application/json')
    else:
        data = JSONParser().parse(request)
        result = pacientes.insert_one(data)
        respo = {
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo,safe =False)

@api_view(['POST'])
def paciente_critico(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    pacientesCriticos = db['pacientesCriticos']
    data = JSONParser().parse(request)
    result = pacientesCriticos.insert_one(data)
    respo = {
        "MongoObjectID": str(result),
        "Message": "nuevo objeto en la base de datos"
    }
    client.close()
    return JsonResponse(respo, safe=False)