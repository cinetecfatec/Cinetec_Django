from django.contrib import admin
from .models import Sessoes,Tabela_preco
from filmes.models import listaFilmes
from django.contrib.admin.widgets import ForeignKeyRawIdWidget

# Register your models here.

class SessoesAdmin(admin.ModelAdmin):
    list_display = ('Id_sessao', 'get_nome_filme', 'data_sessao', 'horario_sessao', 'sala')

    def get_nome_filme(self, obj):
        return obj.Id_filme.nome_filme
    
    get_nome_filme.short_description = 'Nome do Filme'  # Define o cabeçalho da coluna na lista de exibição
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Id_filme':
            kwargs['queryset'] = listaFilmes.objects.all()
            kwargs['widget'] = ForeignKeyRawIdWidget(db_field.remote_field, admin.site)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Sessoes,SessoesAdmin)

class Tabela_precoAdmin(admin.ModelAdmin):
    list_display = ('id_produto','descricao','preco')

admin.site.register(Tabela_preco,Tabela_precoAdmin)