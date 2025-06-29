from Turnos import Turno

class GestorTurnos:
    def asignar_turno(self, paciente, medico, fecha, hora):
        turno = Turno(paciente, medico, fecha, hora)
        paciente.agregar_turno(turno)
        medico.agregar_turno(turno)
        return turno
