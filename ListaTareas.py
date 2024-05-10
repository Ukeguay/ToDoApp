from Tarea import Tarea

# Clase para manejar la lista de tareas
class ListaDeTareas:
    def __init__(self):
        self.tareas = []  # Lista que almacenará las tareas

    def agregar_tarea(self, descripcion):
        # Agrega una nueva tarea a la lista
        self.tareas.append(Tarea(descripcion))
        print("Tarea agregada exitosamente.")

    def marcar_completada(self, posicion):
        # Intenta marcar la tarea en la posición dada como completada
        try:
            self.tareas[posicion].marcar_completada()
            print("Tarea marcada como completada.")
        except IndexError:
            print("Error: posición no válida.")

    def mostrar_tareas(self):
        # Muestra todas las tareas con sus índices y estados
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            print("Lista de tareas pendientes:")
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):
        # Intenta eliminar la tarea en la posición dada
        try:
            del self.tareas[posicion]
            print("Tarea eliminada exitosamente.")
        except IndexError:
            print("Error: posición no válida.")
