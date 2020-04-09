from django.urls import path

from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('cadastre-se/', register, name='register'),
    path('nova-senha/', password_reset, name='password_reset'),
    path('confirmar-nova-senha/<key>', password_reset_confirm, name='password_reset_confirm'),
    path('sair/', auth_views.LogoutView.as_view(next_page='core:home'), name='logout'),
    path('editar/', edit, name='edit'),
    path('editar-senha/', edit_password, name='edit_password')
]