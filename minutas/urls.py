from django.urls import path
from minutas import views

urlpatterns = [
  path('/', views.listado, name='minutas.listado'),
  path('/crear/', views.formularioCrearMinuta, name='minutas.crear'),
  path('/guardar/', views.guardar, name='minutas.guardar'),
  path('/eliminar/<int:id>', views.eliminar, name='minutas.eliminar'),
  path('/editar/<int:id>', views.formularioEditar, name='minutas.editar'),
  path('/ver/<int:id>', views.ver, name='minutas.ver'),
  path('/busqueda/', views.formularioBusqueda, name='minutas.busqueda'),
  path('/resultado/', views.resultadosBusqueda, name='minutas.resultado')
  
]