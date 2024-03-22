from tarea import Tarea
from lista_de_tareas import ListaDeTareas
import os
import sys, signal

def limpiar_pantalla():
    # Comando para limpiar la pantalla según el sistema operativo
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def main():
    lista_de_tareas = ListaDeTareas()
    nombre_archivo = "tareas.txt"  # Nombre del archivo de almacenamiento

    # Cargar tareas al inicio del programa
    lista_de_tareas.cargar_tareas(nombre_archivo)

    while True:
        limpiar_pantalla()
        # pyfiglet.print_figlet(text="task hero", colors='BLUE', font="isometric1")
        print("\n--- Aplicación de Lista de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Marcar Tarea como Completada")
        print("3. Eliminar Tarea")
        print("4. Ver Tareas")
        print("5. Ver Tareas Completadas")
        print("6. Salir")

        eleccion = input("Ingresa tu elección: ")

        if eleccion == "1":
            descripcion = input("Ingresa la descripción de la tarea: ")
            nueva_tarea = Tarea(descripcion)
            lista_de_tareas.agregar_tarea(nueva_tarea)
            print("[+] ¡Tarea agregada exitosamente!")
            pausar_pantalla()

        elif eleccion == "2":
            print("Tareas:")
            print(lista_de_tareas)
            indice_tarea = int(input("Ingresa el índice de la tarea para marcar como completada: ")) - 1
            lista_de_tareas.tareas[indice_tarea].marcar_como_completada()
            print("[+] ¡Tarea marcada como completada!")
            pausar_pantalla()

        elif eleccion == "3":
            print("Tareas:")
            print(lista_de_tareas)
            indice_tarea = int(input("Ingresa el índice de la tarea para eliminar: ")) - 1
            lista_de_tareas.eliminar_tarea(indice_tarea)
            print("[+] ¡Tarea eliminada exitosamente!")
            pausar_pantalla()

        elif eleccion == "4":
            print("Tareas:")
            print(lista_de_tareas)
            pausar_pantalla()

        elif eleccion == "5":
            tareas_completadas = lista_de_tareas.obtener_reporte_de_tareas(completadas=True)
            if tareas_completadas:
                print("[+] Tareas Completadas:")
                for tarea in tareas_completadas:
                    print(tarea)
                    pausar_pantalla()
            else:
                print("[!] No hay tareas completadas.")
                pausar_pantalla()

        elif eleccion == "6":
            print("[!] Guardando y saliendo...")
            pausar_pantalla()
            lista_de_tareas.guardar_tareas(nombre_archivo)
            break

        else:
            print("[!] Opción inválida. Por favor, inténtalo de nuevo.")
            pausar_pantalla()

def pausar_pantalla():
    input("Presiona Enter para continuar...")   

if __name__ == "__main__":
    main()