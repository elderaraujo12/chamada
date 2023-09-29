from django.contrib import admin
from . models import Aluno, AnoLetivo, Aula, Disciplina, Matricula, Professor, Serie

# Register your models here.
admin.site.register(Aluno)
admin.site.register(AnoLetivo)
admin.site.register(Aula)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Professor)
admin.site.register(Serie)

