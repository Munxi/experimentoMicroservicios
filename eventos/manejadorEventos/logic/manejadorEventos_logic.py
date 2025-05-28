import requests
from ..models import Evento
from django.conf import settings


def verificar_doctor(doctor_id):
    try:
        response = requests.get(f"{settings.DOCTORES_MS_URL}/{doctor_id}")
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def verificar_paciente(paciente_ni):
    try:
        response = requests.get(f"{settings.PACIENTES_MS_URL}/{paciente_ni}")
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def create_evento(evento_data):
    doctor_id = evento_data.get('doctor_id')
    paciente_ni = evento_data.get('ni_paciente')
    if not doctor_id or not verificar_doctor(doctor_id):
        raise ValueError(f"Doctor con ID {doctor_id} no encontrado")
    if not paciente_ni or not verificar_paciente(paciente_ni):
        raise ValueError(f"Paciente con NI {paciente_ni} no encontrado")
    evento = Evento(
        ni_paciente=evento_data['ni_paciente'],
        tipo=evento_data['tipo'],
        doctor_id=evento_data['doctor_id'],
        resultado=evento_data.get('resultado'),
        fecha=evento_data['fecha'],
        diagnostico=evento_data.get('diagnostico'),
    )
    evento.save()
    return evento