from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):    
    return render(request, 'core/index.html')

def cadastro_aluno(request):    
    return render(request, 'core/cadastro-aluno.html')

def tela_cadastro(request):    
    return render(request, 'core/tela_cadastro.html')

def presenca(request):    
    return render(request, 'core/tela-presenca.html')

def tela_diretor(request):    
    return render(request, 'core/teladiretor.html')

def turno(request):    
    return render(request, 'core/turno.html')
