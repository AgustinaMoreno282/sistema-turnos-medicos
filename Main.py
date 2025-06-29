from Gestor_usuario import GestorUsuarios
from Gestor_turnos import GestorTurnos
from Visor import Visor

def main():
    gestor_usuarios =GestorUsuarios()
    gestor_turnos = GestorTurnos()
    visor = Visor()

    p1 = gestor_usuarios.registrar_paciente("Ana", "ana@gmail.com")
    p2 = gestor_usuarios.registrar_paciente("lola", "lola@gmail.com")
    p3 = gestor_usuarios.registrar_paciente("agus", "agus@gmail.com")

    m1 = gestor_usuarios.registrar_medico("Carlos", "carlos@gmail.com", "Medico Clinico")
    m2 = gestor_usuarios.registrar_medico("Juana", "juana@gmail.com", "Traumatologia")

    gestor_turnos.asignar_turno(p1, m1, "2025-07-01", "10:00")
    gestor_turnos.asignar_turno(p1, m2, "2025-07-02", "11:00")
    gestor_turnos.asignar_turno(p3, m2, "2025-07-17", "13:00")
    gestor_turnos.asignar_turno(p2, m1, "2025-07-10", "17:00")


   
    visor.mostrar_lista(gestor_usuarios.obtener_pacientes(), "pacientes")
    visor.mostrar_lista(gestor_usuarios.obtener_medicos(), "medicos")

 
    for paciente in gestor_usuarios.obtener_pacientes():
     print(f"\nTurnos de {paciente.get_nombre()}:")
     visor.mostrar_turnos(paciente.get_turnos())

   
    for medico in gestor_usuarios.obtener_medicos():
     print(f"\nTurnos del Dr. {medico.get_nombre()}:")
     visor.mostrar_turnos(medico.get_turnos())

if __name__ == "__main__":
 main()
