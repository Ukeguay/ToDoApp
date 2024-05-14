# Importar las clases necesarias
from ListaTareas import ListaDeTareas

# Función principal para el menú interactivo
def menu():
    
    # Crear una nueva lista de tareas
    lista_de_tareas = ListaDeTareas()

    while True:

        print("\nMenú de opciones:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir\n")

        try:
            # Lee la opción seleccionada por el usuario
            opcion = int(input("Selecciona una opción: "))
            
        except ValueError:
            # Maneja error en caso de que el input no sea un número
            print("Error: opción no válida. Por favor, selecciona un número.")
            continue

        if opcion == 1:
            # Agregar nueva tarea
            tarea = input("Ingresa la descripción de la tarea: ")
            lista_de_tareas.agregar_tarea(tarea)
            
        elif opcion == 2:
            # Marcar tarea como completada
            try:
                posicion = int(input("Ingresa la posición de la tarea a marcar como completada: "))
            except ValueError:
                print("Error: ingresa un número válido.")
                continue
            lista_de_tareas.marcar_completada(posicion)
            
        elif opcion == 3:
            # Mostrar todas las tareas
            lista_de_tareas.mostrar_tareas()
            
        elif opcion == 4:
            # Eliminar una tarea
            try:
                posicion = int(input("Ingresa la posición de la tarea a eliminar: "))
            except ValueError:
                print("Error: ingresa un número válido.")
                continue
            lista_de_tareas.eliminar_tarea(posicion)
            
        elif opcion == 5:
            # Salir del programa
            print("\nHasta luego!!\n")
            break
        
        else:
            # Opción no válida
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")


# Ejecutar el menú interactivo
if __name__ == "__main__":
    menu()