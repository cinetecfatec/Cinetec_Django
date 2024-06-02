from django.db import models
from filmes.models import listaFilmes

# Create your models here.
class Sessoes(models.Model):

    dub_leg_model = [('L','Legendado'), ('D','Dublado')]
    modo_2d_3d_model = [('2','2D'),('3','3D')]
    Id_sessao = models.AutoField(primary_key=True)
    Id_filme = models.ForeignKey(listaFilmes, on_delete=models.CASCADE )
    data_sessao = models.DateField(verbose_name="Data da Sessão")
    horario_sessao = models.TimeField(verbose_name= "Horário da Sessão")
    dub_leg = models.CharField(max_length=1,choices=dub_leg_model)
    modo_2d_3d = models.CharField(max_length=1, choices=modo_2d_3d_model)
    sala = models.IntegerField()
    assentos = models.CharField(max_length=128, default='e' * 128)
    
    class Meta:
      ordering = ['-Id_filme']
    

class Tabela_preco(models.Model):
  id_produto = models.CharField(primary_key=True, max_length=4)
  tipo = models.CharField( max_length= 20)
  descricao = models.CharField(verbose_name="Descrição", max_length= 50)
  preco = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Preço")
  
