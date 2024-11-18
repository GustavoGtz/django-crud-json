#########################################################################################
#                                                                                       #
# Clase User para la gestión de datos utilizando un archivo JSON como almacenamiento.   #
#                                                                                       #
# Esta clase proporciona una alternativa no convencional al uso de bases de datos       #
# en Django, interactuando directamente con un archivo JSON para realizar               #
# operaciones de lectura y escritura. Se implementa para cumplir con requisitos         #
# específicos planteados en Radical Software.                                           #
#                                                                                       #
# Limitaciones:                                                                         #
# - Falta de concurrencia: No se maneja el acceso simultáneo por múltiples usuarios     #
#   o procesos, lo que puede generar conflictos.                                        #
# - Baja escalabilidad: Este enfoque no es adecuado para manejar grandes volúmenes      #
#   de datos debido a su rendimiento limitado.                                          #
# - Baja eficiencia: Las operaciones de entrada y salida son lentas y no están          #
#   optimizadas en comparación con bases de datos tradicionales.                        #
#                                                                                       #
# Consideraciones:                                                                      #
# - Este programa tiene fines demostrativos y no está diseñado para ser utilizado       #
#   en entornos de producción.                                                          #
# - El archivo JSON utilizado como base de datos puede cambiar su estructura,           #
#   por lo que se recomienda realizar una copia de seguridad.                           #
#                                                                                       #
#########################################################################################

import json
import os
from django.conf import settings

JSON_FILE_PATH = os.path.join(settings.BASE_DIR, 'usuarios.json')
  
#########################################################################################
#
#   Clase User
#
#   Esta clase permite realizar operaciones básicas de un CRUD utilizando un archivo JSON.
#   Los atributos de la clase corresponden a los campos dentro de la base de datos, y 
#   las operaciones del CRUD se llevan a cabo mediante los métodos definidos en la clase.
#
#   La clase actúa como un almacenador local de la información y, a través de sus 
#   diferentes métodos, gestiona la actualización y reescritura de los datos en el 
#   archivo JSON.
#
#   Atributos:
#
#   - id: Identificador único del usuario, asignado automáticamente.
#   - name: Nombre del usuario, con un máximo de 100 caracteres.
#   - email: Correo electrónico del usuario, con un máximo de 100 caracteres y único.
#   - phone: Número de teléfono del usuario, con un máximo de 10 dígitos (opcional).
#
#   Consideraciones:
#
#   El nombre de los campos en el archivo JSON debe coincidir con los nombres de los campos
#   en esta clase. De lo contrario, podrían surgir conflictos al intentar realizar las 
#   operaciones de lectura y escritura, lo que podría afectar el funcionamiento esperado.
#
#########################################################################################
class User:
    
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    #########################################################################################
    #
    #   Método get_users
    #
    #   Descripción:
    #   Este método permite obtener todas las entradas almacenadas en la base de datos.
    #
    #   Params: None
    # 
    #   Return: Devuelve una lista que contiene todos los usuarios de la base de datos, 
    #           convertidos en objetos de la clase *User*, si el archivo de la base de datos
    #           existe; Si el archivo no existe, devuelve una lista vacía.
    #
    #########################################################################################
    @staticmethod
    def get_users():
        try:
            with open(JSON_FILE_PATH, 'r') as file:
                data = json.load(file)
                return [User(**user) for user in data]
        except FileNotFoundError:
            return []

    #########################################################################################
    #
    #   Método get_user
    #
    #   Descripción:
    #   Este método permite obtener la entrada de un usuario específico de la base de datos.
    #
    #   Params: id -> Identificador del usuario que se está buscando.
    #
    #   Return: Devuelve un objeto de la clase *User* correspondiente al usuario con la id
    #           proporcionada ; Si no se encuentra el usuario, devuelve None.
    #
    #########################################################################################
    @staticmethod
    def get_user(id):
        users = User.get_users()
        for user in users:
            if user.id == id:
                return user
        return None

    #########################################################################################
    #
    #   Método write_to_file
    #
    #   Descripción:
    #   Este método reescribe completamente el archivo JSON, reemplazando toda su 
    #   información con los datos proporcionados. Los datos se guardan utilizando el formato 
    #   definido en este programa, lo que significa que NO se respetará la estructura 
    #   anterior del archivo si es diferente.
    #
    #   Params: users -> Lista de objetos de la clase *User*
    #
    #   Return: None.
    #
    #########################################################################################
    @staticmethod
    def write_to_file(users):
        with open(JSON_FILE_PATH, 'w') as file:
            # Convierte los datos almacenados en los objetos *User* a diccionarios, 
            # asegurando que coincidan con el formato esperado para su almacenamiento en JSON.
            json.dump([user.__dict__ for user in users], file, indent=4)

    #########################################################################################
    #
    #   Método save_user
    #
    #   Descripción:
    #   Este método guarda la información de un usuario, si el usuario ya está creado, entonces
    #   se actualiza su información, en otro caso se crea una nueva entrada.
    #
    #   Params: self -> El propio objeto con la información local.
    #
    #   Return: None
    #
    #########################################################################################
    def save_user(self):
        users = User.get_users()
        for i, existing_user in enumerate(users):
            # Si la condición se cumple, entonces es una actualización
            if existing_user.id == self.id: 
                users[i] = self # Se reemplaza la entrada antigua con la nueva
                break
        else:
            # Si la condición NO se cumple en todo el ciclo, entonces es una creación
            self.id = max([user.id for user in users] or [0]) + 1
            users.append(self)
        User.write_to_file(users)

    #########################################################################################
    #
    #   Método remove_user
    #
    #   Descripción:
    #   Este método elimina la entrada en la base de datos que coincida con la id local.
    #   almacenada el momento de su llamada.
    #
    #   Params: self -> El propio objeto con la información local.
    #
    #   Return: None
    #
    #########################################################################################
    def remove_user(self):
        # Crea la nueva lista sin incluir la id deseada
        users = [user for user in User.get_users() if user.id != self.id]
        User.write_to_file(users)