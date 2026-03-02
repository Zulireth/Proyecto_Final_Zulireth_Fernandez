'''
=============================================================================
MÓDULO DE GESTIÓN LÓGICA: CATALOGOLOGICA (📗 Verde: Acción)
=============================================================================
PROPÓSITO:
----------
Separar la lógica de control y procesos en un módulo independiente.
Aquí definimos las funciones que procesan, guardan, leen y mueven los datos.

ANALOGÍA DE LA COCINA:
----------------------
- Catálogo = Recetario / Cuaderno.
- Película = Ingrediente / Receta individual.
- Archivo .txt = El cuaderno físico donde escribimos.
=============================================================================
'''

import os # Librería del sistema operativo (para borrar archivos físicos)

class CatalogoPelicula: # 💜 Clase: El Cuaderno de Recetas
    """
    Clase que representa nuestro catálogo, gestionando un archivo .txt 
    para almacenar los datos de forma permanente.
    """
    
    def __init__(self, nombre): # 💚 Función #self es una convención utilizada que permite acceder o modificar variables vinculadas al objeto
        """
        El 'Constructor'. Se ejecuta al preparar el cuaderno.
        
        Verbo: Crear el catálogo de películas.
        Ingrediente: nombre (str) - El título que le daremos a nuestro cuaderno (ej. 'Accion').
        Tarea: 
            Asignar el nombre y construir la ruta del archivo agregando '.txt'.
            Si le pasamos 'Terror', creará la ruta 'Terror.txt'.
        """
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt" # Construye la ruta del archivo usando el nombre del catálogo. Si el usuario ingresa 'MiCatalogo', la ruta será 'MiCatalogo.txt'.

    def agregar(self, pelicula): # 💚 Función
        """
        Escribe un nuevo registro en el cuaderno.
        
        Verbo: Agregar una película.
        Ingrediente: pelicula (Objeto Pelicula) - El ingrediente ya preparado desde modelos.py.
        Tarea: 
            1. Abrir el archivo en modo 'a' (append/añadir al final).
            2. Escribir la versión de texto de la película (usando str()).
            3. Mostrar un mensaje de éxito.
        """
        # 'a' (append): Si el archivo no existe, lo crea. Si existe, no borra lo anterior.
        # with es una forma de manejar archivos que asegura que se cierren correctamente después de usarlos, incluso si ocurre un error. Es como decir "Abre este cuaderno, haz lo que necesites, y luego ciérralo automáticamente".
        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            # str(pelicula) invoca automáticamente a __str__ en modelos.py
            archivo.write(str(pelicula) + "\n")
            
        print(f"Película '{pelicula.nombre}' agregada con éxito a '{self.nombre}'.")

    def listar(self): # 💚 Función
        """
        Lee el cuaderno y muestra todo lo que tiene escrito.
        
        Verbo: Listar películas.
        Ingrediente: Ninguno (lee directamente del disco duro).
        Tarea: 
            1. Intentar abrir el archivo en modo 'r' (read/leer).
            2. Imprimir línea por línea.
            3. Manejar el error (except) si el cuaderno aún no existe.
        """
        try: # Intentamos abrir el archivo para leerlo. Si no existe, se lanza una excepción (FileNotFoundError) que manejamos en el bloque except.
            # 'r' (read): Solo lectura. Si no existe, lanza FileNotFoundError.
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                print(f"\n--- Catálogo de Películas: {self.nombre} ---")
                
                peliculas_encontradas = False
                for linea in archivo:
                    print(f"- {linea.strip()}") # .strip() quita el salto de línea invisible
                    peliculas_encontradas = True
                
                if not peliculas_encontradas:
                    print("El catálogo está vacío. ¡Añade tu primera película!")

                print("------------------------------------------\n")
                
        except FileNotFoundError:
            print(f"El catálogo '{self.nombre}' aún no existe. Agrega una película primero.")
            
    def modificar(self, nombre_pelicula_buscar, pelicula_nueva): 
        # Ingredientes: El nombre de la peli a buscar (texto) y la película nueva (Objeto)
        try: # Intentamos abrir el archivo para leerlo. Si no existe, se lanza una excepción (FileNotFoundError) que manejamos en el bloque except.
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()

            modificado = False
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                for linea in lineas:
                    # Buscamos solo si el nombre coincide en la línea de texto
                    if f"Película: {nombre_pelicula_buscar}" in linea:
                        archivo.write(str(pelicula_nueva) + "\n") # Escribimos la nueva película en lugar de la antigua
                        modificado = True
                    else:
                        archivo.write(linea)
                        
            if modificado:
                print(f"Película '{nombre_pelicula_buscar}' modificada con éxito.")
            else:
                print(f"No se encontró ninguna película llamada '{nombre_pelicula_buscar}'.")
                
        except FileNotFoundError:
            print("El catálogo aún no existe.") 

    def eliminar(self): # 💚 Función
        """
        Tira el cuaderno a la basura.
        
        Verbo: Eliminar catálogo.
        Ingrediente: Ninguno.
        Tarea: 
            1. Usar os.remove() para borrar el archivo físico.
            2. Manejar el error si el archivo ya no existe.
        """
        try:
            os.remove(self.ruta_archivo)
            print(f"Catálogo '{self.nombre}' eliminado correctamente del disco.")
        except FileNotFoundError:
            print("No se pudo eliminar: El archivo no existe o ya fue borrado.")