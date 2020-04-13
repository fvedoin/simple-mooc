from django.urls import path

from .views import index, details, enrollment, announcements, undo_enrollment

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', details, name='details'),
    path('<slug:slug>/inscricao', enrollment, name='enrollment'),
    path('<slug:slug>/cancelar-inscricao', undo_enrollment, name='undo_enrollment'),
    path('<slug:slug>/anuncios', announcements, name='announcements')
]

