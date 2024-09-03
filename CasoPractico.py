#*******************************************************************************
#  Caso Práctico Final: Gestor de tareas
#  Autora: Candy González Delgado
#  Fecha: 03/05/2024
#*******************************************************************************

#Crea la clase Tareas
class Tareas:                
    def __init__(self):      
        #Constructor de la clase, crea la lista
        #@Param self 
        self.tareas = []

    def agregar_tarea(self, tarea):      
        #Método para agregar tareas a la lista con un diccionario 
        #con descripción y estado. 
        #@Param self 
        #@Param string tarea 
        self.tareas.append({'descripcion': tarea, 'completada': False})

    def marcar_completada(self, posicion):  
        #Método para cambiar el estado de una tarea
        #@Param self
        #@Param int posicion 
        try:
            #Marca la tareas como completada
            self.tareas[posicion]['completada'] = True  
            print("Tarea marcada como completada.")
        except IndexError:
            #Muestra un mensaje de error si el número
            #No está en el menú de opciones
            print("La posición ingresada no es válida.")

    def mostrar_tareas(self):                        
        #Muestra la lista de tareas            
        if not self.tareas:
            #Si no hay tareas muestra un mensaje
            print("No hay tareas pendientes.")       
        else:
            #Si hay tareas, para cada tarea muestra el estado
            for i, tarea in enumerate(self.tareas):  
                #Si esta completada o pendiente, con el operador ternario
                estado = "Completada" if tarea['completada'] else "Pendiente"   
                #Muestra por consola con formato la tarea y su estado
                print(f"{i+1}. {tarea['descripcion']} - {estado}")  

    def eliminar_tarea(self, posicion):     
        #Método para eliminar una tarea, 
        #usando el número de la tarea a eliminar
        #@Param self
        #@Param int posicion 
        try:
            #Elimina la tarea de la lista, eliminando la posición
            del self.tareas[posicion]       
            print("Tarea eliminada correctamente.")
        except IndexError:                  
            #Salta si la posición a eliminar no existe
            print("La posición ingresada no es válida.")


def main():
# Función principal para ejecutar el programa
    #Crea una instancia de la clase Tareas en la variable lista_tareas
    lista_tareas = Tareas() 
    while True:             
        #Bucle para mostrar las opciones del menú
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

        #Entrada de datos para escoger que opción se quiere ejecutar
        opcion = input("Seleccione una opción: ")   

        if opcion == '1':              
            #Si se elige la opción 1
            #Pide escribir la descripción de la tarea
            nueva_tarea = input("Ingrese la nueva tarea: ")   
            #Llama al método agregar_tarea con la descripción
            lista_tareas.agregar_tarea(nueva_tarea) 
        elif opcion == '2':            
            #Si se elige la opción 2
            #Llama al método mostrar_tareas()
            lista_tareas.mostrar_tareas()   
            try:
                #Pide el número de la tarea a marcar como completada 
                #y le resta 1 porque el índice de la lista comienza en 0
                posicion = int(input("Ingrese la posición de la tarea que desea marcar como completada: ")) - 1     
                #Llama al método completar con el número de la tarea
                lista_tareas.marcar_completada(posicion)    
            except ValueError:      
                #Salta el mensaje si se escoge un número 
                #que no este en la lista
                print("Por favor ingrese un número válido.")
        elif opcion == '3':
            #Muestra la lista con todas las tareas
            lista_tareas.mostrar_tareas()   
        elif opcion == '4':
            #Muestra la lista con todas las tareas
            lista_tareas.mostrar_tareas()   
            try:
                #Pide el número de la tarea a eliminar 
                #y le resta 1 porque el índice de la lista comienza en 0
                posicion = int(input("Ingrese la posición de la tarea que desea eliminar: ")) - 1   
                #Invoca al método eliminar_tarea con el número escogido
                lista_tareas.eliminar_tarea(posicion) 
            except ValueError: 
                #Salta el mensaje si se escoge un número que no este en la lista
                print("Por favor ingrese un número válido.")
        elif opcion == '5':     
            #Mensaje de despedida
            print("¡Hasta la próxima vez!") 
            #Sale del bucle while
            break       
        else:
            #Muestra este mensaje si se coloca un número que no esté en el menu de opciones
            print("Opción no válida. Por favor seleccione una opción válida.")  


#Pregunta si el archivo está siendo ejecutado como programa principal
if __name__ == "__main__":  
    # Llama a la función main
    main()  


