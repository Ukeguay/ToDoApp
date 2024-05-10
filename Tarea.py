# Clase para representar una tarea
class Tarea:
    
    # El método __init__ es el constructor de la clase, se ejecuta al crear un nuevo objeto.
    def __init__(self, tarea):
        # Almacena el argumento `tarea` en el atributo `tarea` del objeto.
        self.tarea = tarea
        
        # El atributo `completada` se establece en False por defecto.
        # Representa el estado de si la tarea está completada o no.
        self.completada = False

    # Método para marcar la tarea como completada.
    def marcar_completada(self):
        # Cambia el atributo `completada` a True, indicando que la tarea está completada.
        self.completada = True

    # Método especial que define cómo se muestra el objeto como una cadena de texto.
    def __str__(self):
        # Determina el estado de la tarea basado en el atributo `completada`.
        estado = "Completada" if self.completada else "Pendiente"
        
        # Devuelve la descripción de la tarea junto con su estado entre corchetes.
        return f"{self.tarea} [{estado}]"