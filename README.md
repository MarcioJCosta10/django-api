# ------
# criar ambiente virtual --> python3 -m venv ./venv
# --> source venv/bin/activate
# --> pip install django
# --> django-admin startproject setup .
# --> subir o server

# ----------------
# criar api de escola
# criar o app --> parar o server
# --> python3 manage.py startapp escola
# em views.py --> from django.http import JsonResponse
# --> criar a função em views.py 
# def alunos(request):
#    if request.method == 'GET':
#       aluno = {'id':1, 'nome': 'Marcio'}
#       return JsonResponse(aluno)
      
# -----------
# em setup urls.py fazer o import de alunos
# criar o path --> path('alunos/', alunos)

# -----------
# Instalar django rest fremework
# --> pip install djangorestframework
# --> pip install markdown 
# --> rest_framework em setting INSTALLED_APPS 


# ----------
# criar o model
# cria as classes alunos e curso
# registrar os app escola no settings
 # makemigrations
 # migrate


# -----------
# config admin.py para ter crud de alunos e cursos
# em admin.py --> from escola.models import Aluno, Curso
# 

# ------------
# criar superusuário para admin e senha
# --> python3 manage.py createsuperuser
# marcio
# marcio@nmulifibra.com.br
# Nm12345678
# logar no admin localhost:8000/admin
# criar alunos e curso de teste

# ---------------------------
# serializer -- > converte as informações de django para json e de json para django
#  no app de escola criar o serializer.py
# --> from rest_framework import serializers
# --> importar os models que vou serializar --> from escola.models import Aluno, Curso
# # serializer é um filtro de dados que quero disponibilizar para a API--> para entregar os dados armazenados no banco de dados no formato Json por exemplo ou receber um Json
# os dados de saída são serializados
# os dados de entrada serão desserializados


# -----------------
# criar quem é o responsável por selecionar e dizer que vamos usar tal serializer
# em views.py 
# a estrutura REST permite incluir uma abstração para lidar com viewset 
# viewset permite pensar bem na modelagem de negócio sem se preocupar com as interações da API deixando a construção da URL ser criado automaticamente através das convenções comuns

# ------------------------
# mudar views.py
# from rest_framework import viewsets
# quais modelos vamos usar
# from escola.models import Aluno, Curso
# importar os serializers
# from serializer import AlunoSerializer, CursoSerializer

# ----------------
# como criarmos viewset precisamos configurar as rotas para exibir viewsets
# mudar os imports em url.py --> from escola.views import AlunosViewSet, CursosViewSet
# importar rota default para podermos usar a api no navegador
# --> from rest_framework import routers
# criar a rota --> router = routers.DefaultRouter()
# registrar Alunoviewset e Cursoviewset --> 
#                  rota      quem vai atender
# router.register('alunos', AlunosViewSet, basename='Alunos')
# router.register('cursos', CursosViewSet, basename='Cursos')
# incluir as rotas nas urls -->  path('', include(router.urls))
# ao acessar veremos django rest framework com as duas rotas e clicando na url veremos os dados salvo no banco

# ----------------
# crud sem admin
# ainda em DJANGO REST framework  efetuar inclusão de cursos via json e html form

# -----------------------
# Testar a api pelo postman usando: GET, POST, PUT, PATCH, DELETE
# 

# ---------------------
# Criar relacionamentos entre os modelos
# matricular uma aluno a um curso
# em models.py criar a class matricula
# em admin criar propriedade para as matricular
# criar e enviar migrações --> para server
# subir server e visualizar

# ---------------
# exibir as matriculas no Django REST pelo id do aluno?: localhost:8000/aluno/2/matriculas/
# em serializer.py criar a classe serializadora --> ListaMatriculasAlunosSerializer
# em views importar esse serializer --> ListaMatriculasAlunoSerializer
# fazer o import do generic do rest_framework
# passar como parâmetros para a classe o argumento: generics.ListAPIVew
# criar a função para pegar o id do aluno --> get_queryset
# definir o serializer_class --> ListaMatriculasAlunoSerializer
# importar para urls.py ListaMatriculasAluno
# registrar a url em urls.py --> criar novo path
#   path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view())
# fazer o tete e veremos funcionando
# mudar para exibir o nome do curso e o período em serializer.py
# curso = serializers.ReadOnlyField(source='curso.descricao') --> vamos ler os recusos dos cursos
# periodo = serializers.SerializerMethodField() --> usar o mesmo método que estou usando nas 
# config do admin
# criar o método para buscar --> def get_periodo(self, obj):
# return obj.get_periodo_display()

# Após isso conseguimos consular pelo id na rota como está no admin


# -----------------------------------------------------------------
# criar uma autenticação para a API
# em views.py --> from rest_framework.authentication import BasicAuthentication
# em views.py --> from rest_framework.permissions import IsAuthenticated
# nas classes que vamos exigir autenticação criar as variáveis: 
# authentication_class = [BasicAuthentication]
# permission_classes = [IsAuthenticated] 
# 








