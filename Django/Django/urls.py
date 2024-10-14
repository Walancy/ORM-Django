from django.urls import path
from . import views

urlpatterns = [
    path('departamentos/', views.listar_departamentos, name='listar_departamentos'),
    path('departamentos/criar/', views.criar_departamento, name='criar_departamento'),
    path('departamentos/editar/<int:pk>/', views.editar_departamento, name='editar_departamento'),
    path('departamentos/deletar/<int:pk>/', views.deletar_departamento, name='deletar_departamento'),

    path('projetos/', views.listar_projetos, name='listar_projetos'),
    path('projetos/criar/', views.criar_projeto, name='criar_projeto'),
    path('projetos/editar/<int:pk>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/deletar/<int:pk>/', views.deletar_projeto, name='deletar_projeto'),

    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    path('funcionarios/criar/', views.criar_funcionario, name='criar_funcionario'),
    path('funcionarios/editar/<int:pk>/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionarios/deletar/<int:pk>/', views.deletar_funcionario, name='deletar_funcionario'),
]
