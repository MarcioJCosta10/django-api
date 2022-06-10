from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

# Register your models here.
class Alunos(admin.ModelAdmin):
    # campos exibidos no display do admin
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    # permitem edição
    list_display_links = ('id', 'nome')
    # campo de busca
    search_fields = ('nome',)
    # paginação
    list_per_page = 20


 # registrar essa configuração do admin
 #                  model  class
admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)


admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)


admin.site.register(Matricula, Matriculas)
