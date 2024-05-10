from Tarea import Tarea

# Clase para manejar la lista de tareas
class ListaDeTareas:
    
    def __init__(self):
        # Lista que almacenará las tareas
        self.tareas = []

    def agregar_tarea(self, tarea):
        # Agrega una nueva tarea a la lista
        self.tareas.append(Tarea(tarea))
        print("Tarea agregada.")

    def marcar_completada(self, posicion):

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
            print("\nLista de tareas pendientes:")
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):
        # Intenta eliminar la tarea en la posición dada
        try:
            del self.tareas[posicion]
            print("Tarea eliminada exitosamente.")
        except IndexError:
            print("Error: posición no válida.")
