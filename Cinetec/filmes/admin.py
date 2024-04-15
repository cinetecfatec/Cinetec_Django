from django.contrib import admin
from .models import listaFilmes
from django.contrib import admin 
from embed_video.admin import AdminVideoMixin 
from .models import listaFilmes 

# Descomente esta linha se quiser usar AdminVideoMixin
class ListaFilmesAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('id_filme','nome_filme','genero')

admin.site.register(listaFilmes, ListaFilmesAdmin)

