from django.urls import path,include
from . import views  

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('<int:id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),

]
