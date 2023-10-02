from django.urls import path
from apps.gallery.views import (index, imagem, buscar, surpreenda_me, nova_imagem, editar_imagem,
                                deletar_imagem, filtro)

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('surpreenda_me', surpreenda_me, name='surpreenda_me'),
    path('nova_imagem', nova_imagem, name='nova_imagem'),
    path('editar_imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar_imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro')
]
