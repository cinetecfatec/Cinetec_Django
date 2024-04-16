from django.contrib import admin
from .models import listaFilmes
from django.contrib import admin 
from embed_video.admin import AdminVideoMixin 
from .models import listaFilmes,Teste

# Descomente esta linha se quiser usar AdminVideoMixin
class ListaFilmesAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(listaFilmes, ListaFilmesAdmin)
admin.site.register(Teste)
