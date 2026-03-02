'''
=============================================================================
MÓDULO DE DATOS: MODELOS (📘 Azul: Datos)
=============================================================================
PROPÓSITO:
----------
Este archivo contiene los contenedores de información de mi catálogo.
Aquí definimos "qué" es una película y qué datos la componen.

CONCEPTO DE PROGRAMACIÓN:
-------------------------
- CLASES Y OBJETOS: Plantillas para crear entidades.
- ENCAPSULAMIENTO: Proteger datos sensibles (como el nombre).
=============================================================================
'''

class Pelicula: # 💜 Clase: La Receta base
    """
    Aquí definimos la 'Receta' de las películas.
    Es la estructura estandarizada que debe tener cada registro en nuestro catálogo.
    """
    
    def __init__(self, nombrepelicula, genero, duracion, actor_principal, año_lanzamiento): # 💚 Función
        """
        Constructor de la clase Pelicula. Se ejecuta al crear una nueva película.
        
        Verbo: Inicializar datos de la película.
        Ingredientes: 
            - nombrepelicula (str): Título de la peli.
            - genero (str): Categoría.
            - duracion (int/str): Tiempo en minutos.
            - actor_principal (str): Protagonista.
            - año_lanzamiento (int/str): Año de estreno.
        Tarea: 
            Asignar los ingredientes a los atributos de la película. 
            Se incluye validación (try/except) para asegurar que la duración y el año 
            sean números enteros. Si el usuario escribe letras ahí, se pone 0 por defecto.
        """
        # 1. Encapsulamiento del nombre (Doble guion bajo lo hace privado)
        self.__nombre = nombrepelicula
        
        # 2. Atributos públicos directos
        self.genero = genero
        self.actor_principal = actor_principal
        
        # 3. Validación de Duración (Intentar convertir a entero)
        try:
            self.__duracion = int(duracion)
        except ValueError:
            self.__duracion = 0 # Valor por defecto si falla
            
        # 4. Validación de Año (Intentar convertir a entero)
        try:
            self.__año_lanzamiento = int(año_lanzamiento)
        except ValueError:
            self.__año_lanzamiento = 0 # Valor por defecto si falla

    def __str__(self): # 💚 Función
        """
        Método especial de Python para representar el objeto como texto.
        
        Verbo: Representar película como texto.
        Ingrediente: Ninguno (usa los propios atributos del objeto mediante 'self').
        Tarea: 
            Retornar una cadena (string) formateada con toda la información.
            Esto es clave porque es exactamente lo que se escribirá en el archivo .txt.
        """
        return (f"Película: {self.__nombre} | Género: {self.genero} | "
                f"Duración: {self.__duracion} min | Actor: {self.actor_principal} | "
                f"Año: {self.__año_lanzamiento}")

    # --- ZONA DE DECORADORES (ENCAPSULAMIENTO) ---

    @property
    def nombre(self): # 💚 Función
        """
        Método 'getter' (Obtenedor). Permite leer el atributo privado.
        
        Verbo: Obtener nombre de la película.
        Ingrediente: Ninguno.
        Tarea: Retornar el valor oculto en self.__nombre de forma segura.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre): # 💚 Función
        """
        Método 'setter' (Configurador). Permite modificar el atributo privado pasando filtros.
        
        Verbo: Modificar nombre de la película.
        Ingrediente: nuevo_nombre (str) - El nuevo título a asignar.
        Tarea: 
            1. Validar que sea un texto (str).
            2. Validar que no esté vacío.
            3. Guardarlo limpio de espacios innecesarios (.strip()).
        """
        # Validar que el ingrediente sea del tipo 'texto'
        if not isinstance(nuevo_nombre, str):  
            raise ValueError("El nombre debe ser una cadena de texto (puede incluir números, pero debe ser texto).")
    
        # Validar que no esté vacío después de quitarle los espacios
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío ni tener solo espacios.")
    
        # Si pasa las pruebas, actualizamos el atributo privado
        self.__nombre = nuevo_nombre.strip()