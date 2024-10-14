from django import forms
from .models import Departamento, Projeto, Funcionario

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome', 'localizacao']

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'data_inicio', 'data_fim', 'departamento']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'sobrenome', 'email', 'data_admissao', 'departamento', 'projetos']
