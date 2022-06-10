from rest_framework import viewsets, generics
# quais modelos vamos usar
from escola.models import Aluno, Curso, Matricula
# importar os serializers de escola
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos alunos e alunas"""
    # trazer todos alunos
    queryset = Aluno.objects.all()
    # informar qual é o serializer
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
class ListaMatriculasAluno(generics.ListAPIView):
  """Listando as matriculas de um aluno ou aluna"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasAlunoSerializer
  
