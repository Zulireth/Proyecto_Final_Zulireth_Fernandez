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
import os
import platform 

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
    
    # Se añade .strip() como mejora para evitar errores si el usuario presiona espacio por accidente.
    nombre_catalogo = input("Ingresa el nombre del catálogo de películas: ").strip()
    catalogo = CatalogoPelicula(nombre_catalogo)

    while True: # Bucle infinito (se rompe con 'break')
        limpiar_pantalla() 
        print(f"--- 🎬 CATÁLOGO ACTIVO: {catalogo.nombre.upper()} ---")
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Modificar Películas")
        print("4. Eliminar Catálogo de Películas")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ").strip()

        # MATCH-CASE: El inspector de tráfico que decide qué ruta tomar
        match opcion:
            
            case '1':
                # Verbo: Solicitar datos y agregar
                limpiar_pantalla()
                print("--- 🍿 Agregar Nueva Película ---")
                # Usamos .strip() en los inputs de texto por limpieza de datos
                nombre = input("Nombre de la película: ").strip()
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
                print("--- ✏️ Modificar Película ---")
                
                print("1. Ingresa el nombre EXACTO de la película que quieres cambiar:")
                # Aquí solo pedimos y guardamos el texto del nombre
                nombre_v = input("Nombre actual: ").strip()
                
                print("\n2. Ingresa los NUEVOS datos para esta película:")
                nombre_n = input("Nuevo nombre: ").strip()
                genero_n = input("Nuevo género: ").strip()
                duracion_n = input("Nueva duración: ").strip()
                actor_n = input("Nuevo actor principal: ").strip()
                año_n = input("Nuevo año: ").strip()
                
                # Preparamos el único Ingrediente complejo (la película nueva)
                pelicula_nueva = Pelicula(nombre_n, genero_n, duracion_n, actor_n, año_n)
                
                # ¡Ahora sí! Llamamos a la función pasándole el texto (nombre_v) y el objeto nuevo
                catalogo.modificar(nombre_v, pelicula_nueva)
                
                input("\nPresiona Enter para volver al menú...")

            case '4':
                # Verbo: Solicitar eliminación del archivo
                limpiar_pantalla()
                catalogo.eliminar()
                input("\nPresiona Enter para continuar...")
                print("Saliendo del programa, ya que el catálogo fue eliminado.")
                break # Rompe el bucle porque ya no hay catálogo

            case '5':
                # Verbo: Salir voluntariamente
                limpiar_pantalla()
                print("\n¡Hasta luego! Gracias por usar el catálogo de películas. 🍿")
                break # Rompe el bucle para terminar
            
            case _: # Comodín (Else): Si ingresa '5', 'Hola', etc.
                print("\n❌ Opción no válida. Por favor, elige una opción del 1 al 5.")
                input("\nPresiona Enter para intentarlo de nuevo...")

# --- PUNTO DE ENTRADA DEL SCRIPT ---
# Si este archivo se ejecuta directamente (y no es importado por otro), arranca la app. Esto me servira para un futuro proyecto Web con un framework.
if __name__ == "__main__":
    ejecutar_app()
    # Una vez que el bucle 'while' se rompe con un 'break', el código continúa aquí.
    limpiar_pantalla() 
    print("Programa finalizado correctamente.\n")