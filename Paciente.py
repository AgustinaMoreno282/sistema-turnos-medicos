from Usuario import Usuario

class Paciente(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self._turnos = []  # Lista de objetos Turno

    def agregar_turno(self, turno):
        self._turnos.append(turno)

    def get_turnos(self):
        return self._turnos