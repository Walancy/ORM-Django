from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_admissao = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    projetos = models.ManyToManyField(Projeto, related_name='funcionarios')

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
