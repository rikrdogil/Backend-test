from django.db import models

# Create your models here.

class Categoria(models.Model):

    nome = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):

        nome = models.CharField(max_length=200)
        preco = models.FloatField("Preço")
        categoria = models.ManyToManyField(Categoria)
    
        def __str__(self):
          return self.nome
