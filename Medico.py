from Usuario import Usuario

class Medico(Usuario):
    def __init__(self, nombre, email, especialidad):
        super().__init__(nombre, email)
        self._especialidad = especialidad
        self._turnos = []

    def get_especialidad(self):
        return self._especialidad
    
    def agregar_turno(self, turno):
        self._turnos.append(turno)

    def get_turnos(self):
        return self._turnos


    