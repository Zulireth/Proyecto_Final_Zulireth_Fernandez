'''
=============================================================================
MÓDULO DE CONTROL PRINCIPAL: APP.PY (📒 Amarillo: Control)
=============================================================================
PROPÓSITO:
----------
Este es el director de orquesta de nuestro programa.
Se encarga de interactuar con el usuario, mostrar el menú gráfico en 
consola y decidir qué módulos llamar.

CONCEPTO DE PROGRAMACIÓN:
-------------------------
- PUNTO DE ENTRADA: Es el archivo principal que se ejecuta.
- BUCLE INFINITO (WHILE): Mantiene el programa vivo hasta que el usuario sale.
- MATCH-CASE: Estructura moderna para tomar decisiones de menú.
=============================================================================
'''

# 1. Importamos librerías nativas de Python
import os # Librería del sistema operativo (para borrar archivos físicos)
import platform # Librería para detectar el sistema operativo (Windows, Mac, Linux)

# 2. Importamos nuestras clases de los otros módulos (Nuestras "Recetas")
from modelos import Pelicula               # 📘 Datos
from catalogologica import CatalogoPelicula # 📗 Acción

def limpiar_pantalla(): # 💚 Función
    """
    Herramienta visual para que la consola no se llene de texto.
    
    Verbo: Limpiar pantalla.
    Ingrediente: Ninguno.
    Tarea: 
        1. Detectar si el sistema es Windows, Mac o Linux mediante 'platform'.
        2. Enviar el comando adecuado ('cls' o 'clear') a la consola.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def ejecutar_app(): # 💚 Función
    """
    El ciclo de vida principal de la aplicación.
    
    Verbo: Ejecutar aplicación.
    Ingrediente: Ninguno.
    Tarea: 
        1. Solicitar el nombre del catálogo inicial.
        2. Iniciar el bucle 'while True' para mostrar el menú.
        3. Usar 'match-case' para dirigir al usuario a la acción correcta.
    """
    limpiar_pantalla()
    
    print("--- 🎬 BIENVENIDO AL GESTOR DE CATÁLOGOS DE PELÍCULAS ---")
    # Se añade .strip() como mejora para evitar errores si el usuario presiona espacio por accidente.
    nombre_catalogo = input("Para empezar, ingresa el nombre del catálogo: ").strip()
    catalogo = CatalogoPelicula(nombre_catalogo)

    while True: # Bucle infinito (se rompe con 'break')
        limpiar_pantalla() 
        print(f"--- 🎬 CATÁLOGO ACTIVO: {catalogo.nombre.upper()} ---") # upper convierte todos todos los caracteres alfabéticos de una cadena a mayúsculas, devolviendo una nueva cadena sin modificar la original
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Modificar Película")
        print("4. Eliminar Catálogo Actual")
        print("5. Cambiar a otro Catálogo")
        print("6. Salir")
        
        opcion = input("Elige una opción (1-6): ").strip() # strip() elimina los espacios en blanco al inicio y al final de la cadena, lo que ayuda a evitar errores si el usuario presiona espacio por accidente.

        # MATCH-CASE: funciona como un inspector de tráfico que decide qué ruta tomar
        # Utiliza match para evaluar y case para definir patrones, incluyendo un case _ como comodín para manejar opciones no previstas.
        match opcion:
            
            case '1':
                # Verbo: Solicitar datos y agregar
                limpiar_pantalla()
                print(f"--- 🍿 Agregar Nueva Película a '{catalogo.nombre.upper()}' ---") # upper convierte todos los caracteres alfabéticos de una cadena a mayúsculas, devolviendo una nueva cadena sin modificar la original
                
                # Usamos .strip() en los inputs de texto por limpieza de datos
                nombre = input("Nombre de la película: ").strip() # strip() elimina los espacios en blanco al inicio y al final de la cadena, lo que ayuda a evitar errores si el usuario presiona espacio por accidente.
                genero = input("Género: ").strip()
                duracion = input("Duración (min): ").strip()
                actor = input("Actor principal: ").strip()
                año = input("Año de lanzamiento: ").strip()
                
                # Creamos el ingrediente (Objeto Pelicula)
                pelicula_nueva = Pelicula(nombre, genero, duracion, actor, año)
                # Lo mandamos a la función agregar de nuestro catálogo
                catalogo.agregar(pelicula_nueva)
                
                input("\nPresiona Enter para volver al menú...") 

            case '2':
                # Verbo: Solicitar la lista de películas
                limpiar_pantalla()
                catalogo.listar()
                input("\nPresiona Enter para volver al menú...") 
            
            case '3':
                # Verbo: Solicitar modificación de una película
                limpiar_pantalla()
                print(f"--- ✏️ Modificar Película en '{catalogo.nombre.upper()}' ---") # upper convierte todos los caracteres alfabéticos de una cadena a mayúsculas, devolviendo una nueva cadena sin modificar la original
                
                print("1. ¿Qué película quieres modificar?")
                nombre_v = input("Ingresa el nombre EXACTO de la película actual: ").strip()
                
                print("\n2. Ingresa los NUEVOS datos para esta película:")
                nombre_n = input("Nuevo nombre: ").strip() # strip() elimina los espacios en blanco al inicio y al final de la cadena, lo que ayuda a evitar errores si el usuario presiona espacio por accidente.
                genero_n = input("Nuevo género: ").strip()
                duracion_n = input("Nueva duración (min): ").strip()
                actor_n = input("Nuevo actor principal: ").strip()
                año_n = input("Nuevo año: ").strip()
                
                # Preparamos el Ingrediente nuevo
                pelicula_nueva = Pelicula(nombre_n, genero_n, duracion_n, actor_n, año_n)
                
                # Llamamos a la función pasándole el TEXTO a buscar y el OBJETO nuevo
                catalogo.modificar(nombre_v, pelicula_nueva)
                
                input("\nPresiona Enter para volver al menú...")

            case '4':
                # Verbo: Solicitar eliminación del archivo
                limpiar_pantalla()
                print(f"--- 🗑️ Eliminar Catálogo '{catalogo.nombre.upper()}' ---") # upper convierte todos los caracteres alfabéticos de una cadena a mayúsculas, devolviendo una nueva cadena sin modificar la original
                confirmacion = input(f"¿Estás seguro de eliminar '{catalogo.nombre}'? Esta acción no se puede deshacer (s/n): ").strip().lower()
                
                if confirmacion == 's':
                    catalogo.eliminar()
                    input("\nPresiona Enter para continuar...")
                    # Como borramos el cuaderno, obligamos al usuario a elegir uno nuevo
                    limpiar_pantalla()
                    print("El catálogo ha sido eliminado.")
                    nuevo_nombre = input("Por favor, ingresa el nombre de un NUEVO catálogo para continuar: ").strip()
                    catalogo = CatalogoPelicula(nuevo_nombre)
                else:
                    print("Operación cancelada. El catálogo está a salvo.")
                    input("\nPresiona Enter para volver al menú...")

            case '5':
                # Verbo: Cambiar cuaderno de trabajo
                limpiar_pantalla()
                print("--- 🔄 Cambiar de Catálogo ---")
                nuevo_nombre = input("Ingresa el nombre del catálogo que deseas abrir o crear: ").strip()
                
                if nuevo_nombre: 
                    # Simplemente reemplazamos el objeto 'catalogo' por uno nuevo
                    catalogo = CatalogoPelicula(nuevo_nombre)
                    print(f"\n¡Catálogo cambiado! Ahora estás trabajando en '{catalogo.nombre.upper()}'.")
                else:
                    print("\nNombre no válido. Sigues en el catálogo actual.")
                    
                input("\nPresiona Enter para volver al menú...")

            case '6':
                # Verbo: Salir voluntariamente
                limpiar_pantalla()
                print("\n¡Hasta luego! Gracias por usar el gestor de catálogos de películas. 🍿")
                break # Rompe el bucle para terminar
            
            case _: # Comodín (Else)
                print("\n❌ Opción no válida. Por favor, elige una opción del 1 al 6.")
                input("\nPresiona Enter para intentarlo de nuevo...")

# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Este if es una forma estándar en Python de asegurarnos que el código dentro de él solo se ejecute si este archivo es el programa principal que se está ejecutando, y no si se importa como un módulo en otro archivo.
# podrá ser útil para un futuro proyecto Web con un framework, donde este archivo app.py se encargue de arrancar la aplicación.
if __name__ == "__main__":
    ejecutar_app()
    limpiar_pantalla() 
    print("Programa finalizado correctamente.\n")