from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.paginator import Paginator

# Carga la página principal del CRUD, pasando como contexto la lista de usuarios.
def home(request):
    users_per_page = 5  # Número de usuarios que se mostrarán por página.
    users = User.get_users()

    # Paginator estructura la información para manejar la paginación de manera adecuada.
    paginator = Paginator(users, users_per_page) 
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'users': users})


# Carga la página para crear una nueva entrada en la base de datos.
# Si se accede por medio de POST, carga la información del formulario
# para actualizar la base de datos.
def add_user(request):
    success_message = None
    if request.method == 'POST':
        # Obtener los datos ingresados
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user = User(id=None, name=name, email=email, phone=phone)
        user.save_user()
        success_message = 'Datos almacenados correctamente'
    return render(request, 'user_form.html', {'success_message': success_message})

# Carga la página para actualizar una entrada en la base de datos.
# Si se accede por medio de POST, carga la información del formulario
# para actualizar la base de datos.
def edit_user(request, id):
    user = User.get_user(id)
    success_message = None
    if request.method == 'POST':
        # Obtener los datos del usuario
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.save_user()
        success_message = 'Datos almacenados correctamente'
    return render(request, 'user_form.html', {'user': user, 'success_message': success_message})

# Carga la página para visualizar los datos de un usuario
def view_user(request, id):
    user = User.get_user(id)
    return render(request, 'user_view.html', {'user': user})

# Funcion para eliminar usuario de la base de datos
def remove_user(request, id):
    user = User.get_user(id)
    if user:
        user.remove_user()
        messages.success(request, f'Usuario {user.name} (id={id}) eliminado con éxito.')

    return redirect('home')
