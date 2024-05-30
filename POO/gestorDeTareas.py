# ******************************************************************************
# ** Gestor de tareas                                                         **
# ******************************************************************************
class Tareas:                            #Crea la clase tareas
    def __init__(self):                  #Constructor de la clase, crea la lista
        self.tareas = []

    def agregar_tarea(self, tarea):      #Método para agregar tareas a la lista con un diccionario con descripción y estado
        self.tareas.append({'descripcion': tarea, 'completada': False})

    def marcar_completada(self, posicion):  #Método para cambiar el estado de una tarea
        try:
            self.tareas[posicion]['completada'] = True  #Marca la tareas como completada
            print("Tarea marcada como completada.")
        except IndexError:
            print("La posición ingresada no es válida.")

    def mostrar_tareas(self):                        #Muestra la lista de tareas            
        if not self.tareas:
            print("No hay tareas pendientes.")       #Si no hay tareas
        else:
            for i, tarea in enumerate(self.tareas):  #Si hay tareas, para cada tarea muestra el estado
                estado = "Completada" if tarea['completada'] else "Pendiente"   #Si esta completada o pendiente, con el operador ternario
                print(f"{i+1}. {tarea['descripcion']} - {estado}")  #Muestra por consola con formato la tarea y su estado

    def eliminar_tarea(self, posicion):     #Método para eliminar una tarea, recibe como parámetro el número de la tarea a eliminar
        try:
            del self.tareas[posicion]       #Elimina la tarea de la lista, eliminando la posición
            print("Tarea eliminada correctamente.")
        except IndexError:                  #Salta si la posición a eliminar no existe
            print("La posición ingresada no es válida.")


# Función principal para ejecutar el programa
def main():
    lista_tareas = Tareas() #Crea una instancia de la clase Tareas en la variable lista_tareas
    while True:             #Bucle para mostrar las opciones del menú
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")   #Entrada de datos para saber que opción se quiere ejecutar

        if opcion == '1':              #Si se elige la opción 1
            nueva_tarea = input("Ingrese la nueva tarea: ")   #Permite escribir la descripción de la tarea
            lista_tareas.agregar_tarea(nueva_tarea) #Llama al método agregar_tarea con la descripción
        elif opcion == '2':            #Si se elige la opción 2
            lista_tareas.mostrar_tareas()   #llama al método mostrar_tareas() para verlas todas
            try:
                posicion = int(input("Ingrese la posición de la tarea que desea marcar como completada: ")) - 1     #Pide el número de la tarea a marcar como completada y le resta 1 porque el índice de la lista comienza en 0
                lista_tareas.marcar_completada(posicion)    #Llama al método completar con el número de la tarea
            except ValueError:      #Salta si se escoge un número que no este en la lista
                print("Por favor ingrese un número válido.")
        elif opcion == '3':
            lista_tareas.mostrar_tareas()   #Muestra la lista con todas las tareas
        elif opcion == '4':
            lista_tareas.mostrar_tareas()   #Muestra la lista con todas las tareas
            try:
                posicion = int(input("Ingrese la posición de la tarea que desea eliminar: ")) - 1   #Pide el número de la tarea a eliminar y  le resta 1 porque el índice de la lista comienza en 0
                lista_tareas.eliminar_tarea(posicion) #invoca al método eliminar_tarea con el número escogido
            except ValueError: #Salta si se escoge un número que no este en la lista
                print("Por favor ingrese un número válido.")
        elif opcion == '5':     
            print("¡Hasta la próxima vez!") #Mensaje de despedida
            break       #Sale del bucle while
        else:
            print("Opción no válida. Por favor seleccione una opción válida.")  #Muestra este mensaje si se coloca un número que no esté en el menu de opciones


if __name__ == "__main__":  #Pregunta si el archivo está siendo ejecutado como programa principal
    main()  # Este código se ejecuta cuando el archivo se ejecuta directamente


