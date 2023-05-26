from django.shortcuts import render
from .models import Locacao, Filme

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def lista_locacao(request):
    locacoes = Locacao.objects.all() #pegando dados do banco.
    context={'locacoes': locacoes} #preparando os dados para o .html
    return render(request,'core/locacao.html',context)

def lista_filmes(request):
    filmes = Filme.objects.all() #pegando dados do banco.
    context={'filmes': filmes} #preparando os dados para o .html
    return render(request,'core/filmes.html',context)



