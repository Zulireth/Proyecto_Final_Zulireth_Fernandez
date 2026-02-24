'''
Proyecto final del curso de python
El objetivo consiste en desarrollar un programa que permita llevar un registro de
películas aplicando conceptos de programación orientada a objetos.
El funcionamiento esperado es el siguiente:
• Al ejecutar el programa se solicita ingresar el nombre del catálogo de películas:
• Si el catálogo de películas no existe se creará uno nuevo. Este catálogo se va a
guardar en un archivo txt donde posteriormente se guardarán las películas. Si el
catálogo existe se podrá seguir modificando el archivo.
• Se debe mostrar un menú de opciones, que permita realizar las siguientes
operaciones:
1. Agregar Película
2. Listar Películas
3. Eliminar catálogo películas
4. Salir

Funcionamiento de las opciones:
• Agregar Película: se va a solicitar el nombre de la película y esta película se va a
guardar en el archivo txt.
• Listar Peliculas: va a mostrar todas las peliculas del catalogo y guardadas en el archivo
txt.
• Eliminar catálogo: elimina el archivo txt que corresponde al catálogo de películas.
• Salir: debe finalizar el programa mostrando un mensaje al usuario.
Implementación POO:
El programa debe implementar programación orientada a objetos.
Se solicita:
• Clase Pelicula.
* Uno de sus atributos debe ser privado.
• Clase CatalogoPelicula.
* atributo nombre
* atributo ruta_archivo
* métodos: agregar, listar, eliminar
'''
class Pelicula:
    def __init__(self, nombrepelicula, genero, duracion, actor_principal, año_lanzamiento):
        """
        Constructor de la clase Pelicula. Se ejecuta al crear una instancia de Pelicula.
        Ingredientes: nombrepelicula (str), genero (str), duracion (int), actor_principal (str), año_lanzamiento (int).
        Tarea: Inicializar los atributos de la película, validando que duracion y año_lanzamiento sean enteros. Si no lo son, se asigna un valor por defecto de 0. 
        El nombre de la película se almacena en un atributo privado para proteger su acceso directo.
        """
        # 1. Atributos directos
        self.__nombre = nombrepelicula
        self.genero = genero
        self.actor_principal = actor_principal
        
        # 2. Validación y Encapsulamiento de Duración
        try:
            self.__duracion = int(duracion)
        except ValueError:
            self.__duracion = 0
            
        # 3. Validación y Encapsulamiento de Año
        try:
            self.__año_lanzamiento = int(año_lanzamiento)
        except ValueError:
            self.__año_lanzamiento = 0

    def __str__(self):
        """
        Método especial para representar la película como una cadena de texto. 
        Verbo: Representar película como texto.
        Ingrediente: Ninguno (usa los atributos de la instancia).  
        Tarea: Retornar una cadena con toda la información de la película formateada.
        Esto facilita mostrar la información de la película en pantalla o al guardarla en un archivo.
        """
        # Usamos los atributos privados que ya están validados
        return (f"Película: {self.__nombre} | Género: {self.genero} | "
                f"Duración: {self.__duracion} min | Actor: {self.actor_principal} | "
                f"Año: {self.__año_lanzamiento}")

    # Decoradores para el nombre (Encapsulamiento)
    @property
    def nombre(self):
        """
        Método getter para el nombre de la película. Permite acceder al nombre de forma controlada.
        Verbo: Obtener nombre de la película.
        Ingrediente: Ninguno (retorna el nombre almacenado).
        Tarea: Retornar el nombre de la película almacenado en el atributo privado.
        Esto permite proteger el acceso directo al atributo y controlar cómo se obtiene el nombre.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """
        Método setter para el nombre de la película. Permite modificar el nombre de forma controlada.
        Verbo: Modificar nombre de la película.
        Ingrediente: nuevo_nombre (str) que se desea asignar.
        Tarea: Validar el nuevo nombre (por ejemplo, asegurarse de que no esté vacío) y asignarlo al atributo privado.
        Esto permite proteger el acceso directo al atributo y controlar cómo se modifica el nombre.
        """
       # 1. Verificamos que sea un string
       # utilizamos isinstance para asegurarnos de que el nuevo nombre es una cadena de texto. Si no lo es, lanzamos un error.
        if not isinstance(nuevo_nombre, str):
            raise ValueError("El nombre debe ser contener solo letras.")
    
        # 2. Verificamos que no esté vacío
        # utilizamos .strip() para eliminar espacios en blanco al inicio y al final del nuevo nombre. Si después de esto el nombre está vacío, lanzamos un error. 
        if not nuevo_nombre.strip():
            raise ValueError("El nombre de la película no puede estar vacío, ni tener espacios en blanco al inicio o al final.")
    
        # 3. Si todo está bien, asignamos (podemos guardar ya "limpio" con strip)
        self.__nombre = nuevo_nombre.strip()

    # Opcional: Podrías agregar @property para duracion y año_lanzamiento si quisieras
    # leerlos individualmente desde app.py