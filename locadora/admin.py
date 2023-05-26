from django.contrib import admin
from .models import Categoria,Filme,Cliente,Locacao

# Register your models here.

@admin.register(Categoria) 
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nome')

@admin.register(Filme) 
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id_filme', 'titulo', 'valor', 'categoria')

@admin.register(Cliente) 
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nome', 'email')

@admin.register(Locacao) 
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('id_locacao', 'nome', 'data', 'cliente')




 