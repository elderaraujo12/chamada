from django.contrib import admin
from .models import Cadastro_aluno
from .models import Cadastro_funcionario
from .models import Login

admin.site.register(Cadastro_aluno)
admin.site.register(Cadastro_funcionario)
admin.site.register(Login)

# Register your models here.
