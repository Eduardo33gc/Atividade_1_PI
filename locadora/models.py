from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    id_filme = models.CharField(max_length=10)
    titulo = models.TextField()
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Locacao(models.Model):
    id_locacao = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    data = models.DateField()
    filme = models.ManyToManyField(Filme)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



