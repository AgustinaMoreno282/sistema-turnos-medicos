class Turno:
    def __init__(self, paciente, medico, fecha, hora):
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._hora = hora

    def __str__(self):
        return f"{self._fecha} a las {self._hora} - Paciente: {self._paciente.get_nombre()} | Médico: Dr. {self._medico.get_nombre()}"