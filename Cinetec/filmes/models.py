from django.db import models

# Create your models here.

class listaFilmes(models.Model):
   Status_model = [('A','Em Cartaz'),('B','Em Breve'),('C','Em pausa')]
   id_filme = models.AutoField(primary_key=True)
   nome_filme = models.CharField(max_length=50)
   foto_cartaz = models.CharField(max_length=50)
   trailer = models.CharField(max_length=150)
   genero = models.CharField(max_length=30) 
   distribuidora = models.CharField(max_length=30)
   duracao = models.IntegerField(verbose_name="duração")
   elenco = models.CharField(max_length=200)
   sinopse = models.TextField()
   status = models.CharField(max_length=1, choices=Status_model)
   classificacao = models.IntegerField(verbose_name = "classificação")

def __init__(self):
        self.pergunta
