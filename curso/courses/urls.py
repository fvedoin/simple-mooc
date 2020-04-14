from django.urls import path

from .views import (
    index, details, enrollment, undo_enrollment,
    announcements, show_announcement, lessons, lesson, material
)

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', details, name='details'),
    path('<slug:slug>/inscricao', enrollment, name='enrollment'),
    path('<slug:slug>/cancelar-inscricao', undo_enrollment, name='undo_enrollment'),
    path('<slug:slug>/anuncios', announcements, name='announcements'),
    path('<slug:slug>/anuncios/<int:pk>', show_announcement, name='show_announcement'),
    path('<slug:slug>/aulas', lessons, name='lessons'),
    path('<slug:slug>/aulas/<int:pk>/', lesson, name='lesson'),
    path('<slug:slug>/materiais/<int:pk>/', material, name='material')
]

