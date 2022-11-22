from django.contrib import admin
from challenge.models import Video, Categoria


class Videos(admin.ModelAdmin):
    list_display = ('id','titulo', 'descricao', 'url','categoriaId')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_filter = ('categoriaId',)
    list_editable = ('categoriaId',)
    list_per_page = 25
    ordering = ('titulo',)

admin.site.register(Video, Videos)

class Categorias(admin.ModelAdmin):
    list_display = ('id','titulo', 'cor')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20

admin.site.register(Categoria, Categorias)


