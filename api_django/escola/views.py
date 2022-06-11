from rest_framework import viewsets, generics
# quais modelos vamos usar
from escola.models import Aluno, Curso, Matricula
# importar os serializers de escola
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
# importar o autenticador
from rest_framework.authentication import BasicAuthentication
# importar quem ira exibir a autenticação
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos alunos e alunas"""
    # trazer todos alunos
    queryset = Aluno.objects.all()
    # informar qual é o serializer
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]  
    permission_classes = [IsAuthenticated]  
    
class ListaMatriculasAluno(generics.ListAPIView):
  """Listando as matriculas de um aluno ou aluna"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasAlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  
class ListaAlunosMatriculados(generics.ListAPIView):
  """ Listando alunos matriculados em um curso"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaAlunosMatriculadosSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
   