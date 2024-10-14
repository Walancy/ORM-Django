from django.shortcuts import render, get_object_or_404, redirect
from .models import Departamento, Projeto, Funcionario
from .forms import DepartamentoForm, ProjetoForm, FuncionarioForm

# -----------departamentos

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'minhaempresa/listar_departamentos.html', {'departamentos': departamentos})

def criar_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'minhaempresa/criar_departamento.html', {'form': form})

def editar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'minhaempresa/editar_departamento.html', {'form': form})

def deletar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        departamento.delete()
        return redirect('listar_departamentos')
    return render(request, 'minhaempresa/deletar_departamento.html', {'departamento': departamento})

# -----------projetos

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'minhaempresa/listar_projetos.html', {'projetos': projetos})

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'minhaempresa/criar_projeto.html', {'form': form})

def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'minhaempresa/editar_projeto.html', {'form': form})

def deletar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('listar_projetos')
    return render(request, 'minhaempresa/deletar_projeto.html', {'projeto': projeto})

# -----------funcionarios

def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'minhaempresa/listar_funcionarios.html', {'funcionarios': funcionarios})

def criar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm()
    return render(request, 'minhaempresa/criar_funcionario.html', {'form': form})

def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'minhaempresa/editar_funcionario.html', {'form': form})

def deletar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('listar_funcionarios')
    return render(request, 'minhaempresa/deletar_funcionario.html', {'funcionario': funcionario})
