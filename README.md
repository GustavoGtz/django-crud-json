# django-crud-json

CRUD en Django utilizando un archivo JSON como base de datos, implementado como parte de una entrevista de trabajo por parte de Radical Software.

Este proyecto fue desarrollado utilizando Python y el Framework Django. En lugar de una base de datos tradicional como MySQL o PostgreSQL, se emplea un archivo JSON como sistema de almacenamiento de datos. Esta implementación es no convencional, ya que Django normalmente trabaja con bases de datos SQL para manejar datos de manera eficiente. En este caso, el archivo JSON es utilizado como un almacenamiento simple y directo, que permite realizar operaciones básicas de CRUD.

## Consideraciones

- **Limitaciones del uso de JSON como base de datos:**
  - **Falta de concurrencia:** Este enfoque no maneja el acceso simultáneo por múltiples usuarios, lo que podría generar conflictos.
  - **Escalabilidad limitada:** Este método no es adecuado para manejar grandes volúmenes de datos debido a las limitaciones de rendimiento.
  - **Eficiencia reducida:** Las operaciones de entrada y salida son más lentas comparadas con las bases de datos tradicionales.
  
Este enfoque fue implementado de manera no convencional para cumplir con los requisitos específicos de la entrevista, adaptándose a un caso donde se necesitaba interactuar con datos de manera ligera y rápida, sin la complejidad de un sistema de gestión de bases de datos tradicional.

Este enfoque se implementó principalmente con fines educativos y no está diseñado para aplicaciones de producción.

## Pasos para ejecutar el programa:

1. **Clona este repositorio:**
   ```bash
   git clone <url-del-repositorio>


cd django-crud-json
python -m venv env
source env/bin/activate  # Para sistemas Unix
env\Scripts\activate     # Para Windows
pip install -r requirements.txt

python manage.py runserver

Notas adicionales
Asegúrate de que el archivo JSON esté en el formato correcto y que los campos coincidan con los especificados en el código para evitar posibles conflictos al intentar acceder o modificar los datos.
Este proyecto está diseñado para propósitos educativos y es una alternativa al uso convencional de bases de datos en Django.
Para cualquier duda o consulta:
Si tienes alguna pregunta sobre la implementación o necesitas más detalles, no dudes en contactar a [tu-email@dominio.com].