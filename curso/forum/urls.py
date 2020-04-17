from django.urls import path

from .views import index, thread, reply_correct, reply_incorrect

urlpatterns = [
    path('', index, name='index'),
    path('tag/<tag>', index, name='index_tagged'),
    path('<slug>', thread, name='thread'),
    path('respostas/<int:pk>/correta', reply_correct, name='reply_correct'),
    path('respostas/<int:pk>/incorreta', reply_incorrect, name='reply_incorrect')
]