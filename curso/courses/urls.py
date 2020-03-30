from django.urls import path

from curso.courses.views import index, details

urlpatterns = [
    path('todos/', index, name='index'),
    path('details/<int:pk>/', details, name='details')
]
