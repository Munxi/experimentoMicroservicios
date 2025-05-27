from ..models import Evento
from informacionPaciente.models import Paciente

def create_evento(evento_data):
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
