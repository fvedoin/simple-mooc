from django.urls import path

from .views import index, details

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', details, name='details'),
]

