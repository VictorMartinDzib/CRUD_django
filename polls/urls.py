
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('editar/<id>/', views.editar, name='editar'),
    path('eliminar/<id>/', views.eliminar, name='eliminar'),
    path('agregar/', views.agregar, name='agregar'),
    path('actualizar/<id>', views.actualizar, name='actualizar'),
    path('guardar/', views.guardar, name='guardar'),
]
