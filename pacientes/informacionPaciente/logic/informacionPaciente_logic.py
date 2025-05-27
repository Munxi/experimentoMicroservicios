from ..models import Paciente
def get_paciente(ni_pk):
    paciente = Paciente.objects.get(pk=ni_pk)
    return paciente
def create_paciente(pac):
    paciente = Paciente(nombres = pac['nombres'],
                        apellidos = pac['apellidos'],
                        NI = pac['NI'],
                        edad = pac['edad'],
                        sexo = pac['sexo'],
                        eps= pac['eps'])
    paciente.save()
    return paciente