from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('tag/<tag>', index, name='index_tagged'),
]