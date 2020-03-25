from django.urls import path

from curso.core.views import home, contact

urlpatterns = [
    path('home/', home, name='home'),
    path('contact/', contact, name='contact')
]
