from django.contrib import admin
from .models import Produto

"""
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'data_criacao')
    search_fields = ('nome',)
    list_filter = ('data_criacao',)
    prepopulated_fields = {'slug': ('nome',)}  # caso tenha campo slug
"""

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'data_criacao')
    search_fields = ('nome',)
    list_filter = ('data_criacao',)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'preco')
        }),
        ('Estoque e Imagem', {
            'fields': ('estoque', 'imagem')
        }),
    )

    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }