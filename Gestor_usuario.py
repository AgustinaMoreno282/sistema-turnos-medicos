from Paciente import Paciente
from Medico import Medico

class GestorUsuarios:
    def __init__(self):
        self._pacientes = []
        self._medicos = []

    def registrar_paciente(self, nombre, email):
        paciente = Paciente(nombre, email)
        self._pacientes.append(paciente)
        return paciente

    def registrar_medico(self, nombre, email, especialidad):
        medico = Medico(nombre, email, especialidad)
        self._medicos.append(medico)
        return medico

    def obtener_pacientes(self):
        return self._pacientes

    def obtener_medicos(self):
        return self._medicos

