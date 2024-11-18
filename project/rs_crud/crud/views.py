from django.shortcuts import render, redirect
from .models import User

# Carga la página principal del CRUD, pasando como contexto la lista de usuarios
def home(request):
    users = User.get_users()
    return render(request, 'home.html', {'users': users})

# Carga la página para crear una nueva entrada en la base de datos.
# Si se accede por medio de POST, carga la información del formulario
# para actualizar la base de datos y redirigir al ...

# TODO: Determinar si al completar el POST, se envie devuelta a home, se mande una alerta o que se hara.
def add_user(request):
    if request.method == 'POST':
        # Obtener los datos ingresados
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user = User(id=None, name=name, email=email, phone=phone)
        user.save_user()
        return redirect('home')
    return render(request, 'user_form.html')

# Carga la página para actualizar una entrada en la base de datos.
# Si se accede por medio de POST, carga la información del formulario
# para actualizar la base de datos y redirigir al ...
# TODO: Determinar si al completar el POST, se envie devuelta a home, se mande una alerta o que se hara.
def edit_user(request, id):
    user = User.get_user(id)
    if request.method == 'POST':
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.save_user()
        return redirect('home')
    return render(request, 'user_form.html', {'user': user})


# Funcion para eliminar usuario de la base de datos
# TODO: Determinar si al completar el POST, se envie devuelta a home, se mande una alerta o que se hara.
def remove_user(request, id):
    user = User.get_user(id)
    if user:
        user.remove_user()
    return redirect('home')
