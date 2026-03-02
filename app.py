'''
=============================================================================
MÓDULO DE CONTROL PRINCIPAL: APP.PY (con Match-Case)
=============================================================================
Este es el director de orquesta de nuestro programa.

PROPÓSITO:
----------
- Gestionar la interacción con el usuario.
- Mostrar el menú de opciones usando una estructura match-case.
- Decidir qué funciones de otros módulos llamar según la elección del usuario.
=============================================================================
'''

# 📒 app.py (Amarillo: Control)

# Importamos las librerías necesarias
import os
import platform # Usaremos esta para detectar el sistema operativo. Esta es una librería estándar de Python que puede decirnos información 
# sobre el sistema en el que se ejecuta el código, como su nombre ("Windows", "Linux", "Darwin" para macOS).

# Importamos nuestras clases
from modelos import Pelicula
from catalogologica import CatalogoPelicula

def limpiar_pantalla():
    """
    Función para limpiar la pantalla de la terminal.
    Me pareció interesante agregar esta función para que detecte en qué sistema operativo se está ejecutando el programa y use el comando correcto.
    Verbo: Limpiar pantalla.
    Detecta el sistema operativo y usa el comando correcto.
    """
    # Si el sistema es Windows, usa 'cls'
    if platform.system() == "Windows":
        os.system("cls")
    # Si es macOS o Linux, usa 'clear'
    else:
        os.system("clear")

def ejecutar_app():
    """
    Función principal que ejecuta el flujo de la aplicación.
    """
    nombre_catalogo = input("Ingresa el nombre del catálogo de películas: ")
    catalogo = CatalogoPelicula(nombre_catalogo)

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar Catálogo de Películas")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")

        # Usamos match-case para manejar la opción del usuario
        # Es una alternativa más limpia a los if/elif/else
        match opcion:
            case '1':
                # Verbo: Solicitar datos de la película
                print("\n--- Agregar Nueva Película ---")
                nombre = input("Nombre de la película: ")
                genero = input("Género: ")
                duracion = input("Duración (min): ")
                actor = input("Actor principal: ")
                año = input("Año de lanzamiento: ")
                
                pelicula_nueva = Pelicula(nombre, genero, duracion, actor, año)
                catalogo.agregar(pelicula_nueva)

            case '2':
                # Verbo: Listar películas
                catalogo.listar()

            case '3':
                # Verbo: Eliminar catálogo
                catalogo.eliminar()
                print("Saliendo del programa, ya que el catálogo fue eliminado.")
                break # Rompemos el bucle para terminar

            case '4':
                # Verbo: Salir del programa
                print("\n¡Hasta luego! Gracias por usar el catálogo de películas.")
                break # Rompemos el bucle para terminar
            
            case _: # El guion bajo (_) actúa como el "else"
                # Se ejecuta si la opción no coincide con ningún case anterior
                print("\nOpción no válida. Por favor, elige una opción del 1 al 4.")
    
    # Este return es opcional, pero indica que la función del bucle ha terminado.
    return

# Punto de entrada del programa
# Agregar el código dentro de este if asegura que el archivo se pueda reutilizar y que sea modular, es decir, que otras partes del programa puedan
# importar funciones de este archivo sin ejecutar el código principal.
if __name__ == "__main__":
    ejecutar_app()
    limpiar_pantalla() # Limpiamos la pantalla al finalizar el programa
    print("\nPrograma finalizado.")