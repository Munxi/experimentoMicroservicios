import requests
from django.core.exceptions import ValidationError
from ..models import Evento
from informacionPaciente.models import Paciente


def verificar_doctor(doctor_id):
    try:
        response = requests.get(f"http://10.128.0.85:8080/doctores/{doctor_id}")
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def create_evento(evento_data):
    
    doctor_id = evento_data.get('doctorEncargado')
    if not doctor_id or not verificar_doctor(doctor_id):
        raise ValueError(f"Doctor con ID {doctor_id} no encontrado")
    
    paciente_ni = evento_data.get('paciente_ni')
    paciente = Paciente.objects.get(NI=paciente_ni)
    evento = Evento(
        paciente=paciente,
        tipo=evento_data['tipo'],
        doctorEncargado=evento_data['doctorEncargado'],
        resultado=evento_data.get('resultado'),
        fecha=evento_data['fecha'],
        diagnostico=evento_data.get('diagnostico'),
    )
    evento.save()
    return evento