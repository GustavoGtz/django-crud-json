# django-crud-json
## CRUD en Django utilizando JSON como base de datos

---

Este repositorio es una prueba técnica para el reclutamiento en Radical Software. Sin embargo, también resulta útil para aquellos interesados en desarrollar un prototipo de página web utilizando un archivo JSON en vez de una base de datos convencional.

---

## Consideraciones

Es importante recalcar que este programa no pretende ser eficiente ni competitivo; solo es una prueba técnica y no se recomienda el uso de archivos JSON como base de datos en entornos de producción.

El archivo JSON será editado continuamente durante la ejecución del programa. Por lo tanto, es recomendable guardar una copia de seguridad en caso de estar trabajando con archivos importantes. Además, los nombres de los campos dentro del JSON deben coincidir con los del programa para evitar problemas.

---

## Uso del programa

Para efectos prácticos, las versiones del software utilizado son:
- Python 3.10.9
- Django 4.2

De preferencia, para correr este programa, utiliza el ambiente `.env` que se encuentra en el repositorio.

### Pasos para ejecutar el proyecto:

1. Clona el repositorio a tu carpeta local utilizando Git:

    ```bash
    git clone https://github.com/GustavoGtz/django-crud-json.git
    ```

    o con SSH

    ```bash
    git clone git@github.com:GustavoGtz/django-crud-json.git
    ```

3. Dentro de la consola de comandos (con el ambiente cargado), colócate en la ruta donde se encuentra el archivo `manage.py` y ejecuta el siguiente comando:

    ```bash
    python manage.py runserver
    ```

4. Ingresa a la ruta proporcionada por la consola (tu IP seguida de un puerto) y agrega el prefijo `/users` para acceder al sitio web. Es decir:

    ```text
    https://ooo.o.o.o:oooo/users
    ```

---

## Acerca de este proyecto

Este es un CRUD en Django utilizando un archivo JSON como base de datos, implementado como parte de una entrevista de trabajo por parte de Radical Software.

---

Si tienes alguna pregunta sobre la implementación o necesitas más detalles, no dudes en contactarme a [gustavogtznav@gmail.com](mailto:gustavogtznav@gmail.com).
