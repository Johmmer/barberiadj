from django.urls import path
from . import views

urlpatterns = [
    path('', views.citas, name='citas'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('ver/', views.ver_cita, name='ver_cita'),
    path('editar/<int:pk>/', views.editar_cita, name='editar_cita'),
    path('cancelar/<int:pk>/', views.cancelar_cita, name='cancelar_cita'),
    path('cita-creada/<int:cita_id>', views.cita_creada, name='cita_creada'),
]
