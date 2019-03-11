from django.db import models

# Create your models here.

class Produto(models.Model):

        nome = models.CharField(max_length=200)
        preco = models.FloatField("Preço")
    
        def __str__(self):
          return self.nome
