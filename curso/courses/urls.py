from django.urls import path

from .views import index, details, enrollment, announcements

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', details, name='details'),
    path('<slug:slug>/inscricao', enrollment, name='enrollment'),
    path('<slug:slug>/anuncios', announcements, name='announcements')
]

