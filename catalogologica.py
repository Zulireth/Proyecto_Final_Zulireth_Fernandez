'''
=============================================================================
MÓDULO DE GESTIÓN LOGICA: CATALOGOLOGICA
=============================================================================
Este módulo contiene las funciones necesarias para la gestión de catálogos.

PROPÓSITO:
----------
Separar la lógica de control y procesos en un módulo independiente,
promoviendo la MODULARIZACIÓN y REUTILIZACIÓN de código.

FUNCIONES:
----------
- Realizar acciones sobre un archivo de texto (.txt) donde se guardan todas las películas.

CONCEPTO DE PROGRAMACIÓN:
-------------------------
- MODULARIZACIÓN: Dividir el código en módulos más pequeños y manejables
- SEPARACIÓN DE RESPONSABILIDADES: Cada módulo tiene una función específica
- REUTILIZACIÓN: Este módulo puede ser importado por múltiples archivos
=============================================================================
'''

#utilice analogia de cocina para explicar el funcionamiento del programa:
# El catálogo de películas es como una receta de cocina.
# Cada película es un ingrediente para agregar a mi receta.
# El archivo .txt es como mi cuaderno de recetas donde escribo todos los ingredientes (películas) que se agregan.
# Cuando quiero agregar una película, es como si estuvieras escribiendo un nuevo ingrediente en mi cuaderno.
# Cuando quiero listar las películas, es como si estuvieras leyendo mi cuaderno para ver todos los ingredientes que he anotado.
# Y cuando quiero eliminar el catálogo, es como si estuvieras tirando mi cuaderno a la basura, borrando toda la información que tenía escrita sobre mis recetas (películas). 

#También utilice la analogía de verbos para explicar el funcionamiento de cada función, así la tarea de cada función se vuelve más clara para mí. 
# Por ejemplo, en la función agregar, el verbo es "Agregar una película", en listar es "Listar películas" y en eliminar es "Eliminar catálogo". 
# Esto me ayuda a entender mejor qué hace cada función y cómo se relaciona con las acciones que quiero realizar sobre mi catálogo de películas.

import os # Necesitaremos esta librería para borrar el archivo físico después

class CatalogoPelicula: # 💜 Clase
    """
        Clase que representa un catálogo de películas, gestionando un archivo .txt para almacenar los datos.
        El 'Constructor'. Se ejecuta al crear el catálogo.
        Ingrediente: El nombre del catálogo (ej: 'Terror').
        Tarea: Guardar el nombre y crear la ruta del archivo .txt.
    """
    def __init__(self, nombre): # 💚 Funciones
        """
        Función constructor de la clase CatalogoPelicula. Se ejecuta al crear una instancia de CatalogoPelicula.
        Verbo: Crear catálogo de películas.
        Ingrediente: nombre (str) - el nombre del catálogo. Esta es una analogía que hago para comprender que el nombre del catálogo es como
        el título de una receta, que luego se usará para nombrar el archivo donde se guardarán las películas.
        Tarea: Inicializar los atributos del catálogo, incluyendo la ruta del archivo .txt donde se guardarán las películas.
        El nombre del catálogo se utiliza para nombrar el archivo .txt (ej: 'Terror.txt').
        Esto permite organizar los catálogos de películas en archivos separados según su nombre.
        """
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"

    def agregar(self, pelicula): # 💚 Funciones
        """
        Función para agregar una película al catálogo. Se ejecuta cuando el usuario elige la opción de agregar película.
        Verbo: Agregar una película.
        Ingrediente: Un objeto de la clase Pelicula (el que definimos en modelos.py). Esta es una analogía que hago para comprender que la película es 
        como un ingrediente que queremos agregar a nuestra receta (catálogo).
        Tarea: Abrir el archivo .txt en modo 'a' (append) y escribir el nombre.
        Si el archivo no existe, se crea automáticamente al abrirlo en modo 'a'.
        """
        # 'a' significa 'append' (agregar al final sin borrar lo anterior)
        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            # Uso str(pelicula) para invocar automáticamente el método __str__ de la clase Pelicula
            archivo.write(str(pelicula) + "\n")
        print(f"Película '{pelicula.nombre}' agregada con éxito.")

    def listar(self):
        """
        Función para listar todas las películas del catálogo. Se ejecuta cuando el usuario elige la opción de listar películas.
        Verbo: Listar películas.
        Ingrediente: Ninguno (lee directamente del archivo).
        Tarea: Leer el archivo y mostrar cada línea con toda la info de la película formateada.
        Si el archivo no existe, se muestra un mensaje informativo.
        """
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                print(f"\n--- Catálogo de Películas: {self.nombre} ---")
                peliculas_encontradas = False
                for linea in archivo:
                    print(f"- {linea.strip()}") # Agrego un guion para mejorar la legibilidad
                    peliculas_encontradas = True
                
                if not peliculas_encontradas:
                    print("El catálogo está vacío. ¡Añade tu primera película!")

                print("------------------------------------------\n")
        except FileNotFoundError:
            print("El catálogo aún no existe. Agrega una película primero.")

    def eliminar(self):
        """
        Función para eliminar el catálogo de películas. Se ejecuta cuando el usuario elige la opción de eliminar catálogo.
        Verbo: Eliminar catálogo.
        Ingrediente: Ninguno.
        Tarea: Borrar el archivo .txt de la computadora usando os.remove().
            Si el archivo existe, se borra y se muestra un mensaje de éxito.
            Si el archivo no existe, se muestra un mensaje informativo.
        """
        try:
            os.remove(self.ruta_archivo)
            print(f"Catálogo '{self.nombre}' eliminado correctamente.")
        except FileNotFoundError:
            print("No se pudo eliminar: El archivo no existe.")