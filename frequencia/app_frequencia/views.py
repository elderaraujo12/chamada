from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):    
    return render(request, 'app_frequencia/index.html')

def cadastro_aluno(request):    
    return render(request, 'app_frequencia/cadastro-aluno.html')

def tela_cadastro(request):    
    return render(request, 'app_frequencia/tela_cadastro.html')

def presenca(request):    
    return render(request, 'app_frequencia/tela-presenca.html')

def tela_diretor(request):    
    return render(request, 'app_frequencia/teladiretor.html')

def turno(request):    
    return render(request, 'app_frequencia/turno.html')
