from django.urls import path

from .views import index, thread

urlpatterns = [
    path('', index, name='index'),
    path('tag/<tag>', index, name='index_tagged'),
    path('<slug>', thread, name='thread'),
]