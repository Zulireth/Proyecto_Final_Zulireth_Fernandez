# 🎬 Proyecto Final: Gestión de Catálogo de Películas  (POO en Python)
**Autora:** Zulireth Fernández  
**Utilice una Metodología de aprendizaje basada en colores y anañogía con la cocina:**

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar un catálogo de películas. Fue creado como proyecto final para aplicar conceptos de Programación Orientada a Objetos (POO), manejo de archivos y modularización.

## 🧠 Metodología de Aprendizaje Aplicada
El código de este proyecto está documentado utilizando un sistema de aprendizaje propio basado en:
*   **Colores**: Para identificar rápidamente la responsabilidad de cada archivo y bloque.
    *   📘 **Azul (Datos):** Modelos y estructuras.
    *   📗 **Verde (Acción):** Lógica, procesamiento y guardado de datos.
    *   📒 **Amarillo (Control):** Menús, interacción con el usuario y flujo principal.
    *   💜 **Morado:** Clases.
    *   💚 **Verde:** Funciones/Métodos.
*   **Analogías**: Se utiliza la analogía de la "Cocina" (Catálogo = Cuaderno de Recetas, Película = Ingrediente).
*   **Estructura Verbo/Ingrediente/Tarea**: Todos los comentarios de funciones describen *qué hace*, *qué recibe* y *cómo lo ejecuta*.

## 📁 Estructura del Proyecto

El proyecto está dividido en tres módulos principales para garantizar la separación de responsabilidades:

1.  **`modelos.py`**: Define la clase `Pelicula`, encargada de validar y encapsular los datos individuales de cada película (nombre, género, duración, etc.).
2.  **`catalogologica.py`**: Define la clase `CatalogoPelicula`, encargada de gestionar el archivo de texto (`.txt`) donde se guardan las películas (agregar, listar, eliminar, modificar).
3.  **`app.py`**: El punto de entrada del programa. Contiene el bucle principal (`while True`), el menú interactivo basado en `match-case` y la interacción directa con el usuario.

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos:
- **Python 3.10 o superior** (requerido para el uso de la estructura `match-case` en el menú principal).

### Pasos:
1. Clona o descarga este repositorio en tu computadora.
2. Abre tu terminal o consola de comandos.
3. Navega hasta la carpeta donde se encuentran los archivos.
4. Ejecuta el archivo principal con el siguiente comando:
   ```bash
   python app.py