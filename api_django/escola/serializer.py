
from dataclasses import fields
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


# Qual é modelos e quais campos utilizado em cada serializer
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
  curso = serializers.ReadOnlyField(source='curso.descricao')
  periodo = serializers.SerializerMethodField()
  class Meta:
    model = Matricula
    fields = ['curso', 'periodo']
# self é a instancia que estamos usando   
# obj é o objeto 
  def get_periodo(self, obj):
    return obj.get_periodo_display()
   
  