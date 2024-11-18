from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.home, name='home'),
    path('users/add/', views.add_user, name='add_user'),
    path('edit/<int:id>/', views.edit_user, name='edit_user'),
    path('remove/<int:id>/', views.remove_user, name='remove_user'),
    path('view/<int:id>/', views.view_user, name='view_user')
]