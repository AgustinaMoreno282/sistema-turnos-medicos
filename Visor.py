class Visor:
    def mostrar_usuario(self, usuario):
        print(f"Nombre: {usuario.get_nombre()}, Email: {usuario.get_email()}")

    def mostrar_medico(self, medico):
        print(f"Dr. {medico.get_nombre()}, Especialidad: {medico.get_especialidad()}, Email: {medico.get_email()}")

    def mostrar_turnos(self, turnos):
        for t in turnos:
            print(t)

    def mostrar_lista(self, lista, tipo):
        print(f"\nLista de {tipo}:")
        for item in lista:
            if tipo == "pacientes":
                self.mostrar_usuario(item)
            elif tipo == "medicos":
                self.mostrar_medico(item)
