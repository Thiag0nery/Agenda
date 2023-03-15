from django.contrib import admin
# Importação do arquivo models
from .models import Contegoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    #Faz refencia ao banco
    list_display= ('id', 'nome', 'sobrenome', 'telefone', 'contegoria', 'mostra')
    #Disponibilizar link nos nomes
    list_display_links = ('id', 'nome')
    list_filter = ('id','nome')
    list_per_page = 10
    search_fields = ('nome','sobrenome')
    list_editable = ('telefone', 'mostra')


admin.site.register(Contegoria)
admin.site.register(Contato, ContatoAdmin)