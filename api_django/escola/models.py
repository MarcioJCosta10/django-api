from statistics import mode
from django.db import models

# Create your models here. columns in tables in database
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField(max_length=30)

    # representar o aluno pelo nome no admin
    def __str__(self):
        return self.nome


class Curso(models.Model):
    # Variável de instância
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediario'),
        ('A', 'Avançado')
    )
    codigo_curso = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL,
                             blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    # cada matricula terá um aluno e curso que terá a FK
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    # tb que manda a FK  se um aluno for deletado tbm deletar matricula
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(
        max_length=1, choices=PERIODO, blank=False, null=False, default='M')
