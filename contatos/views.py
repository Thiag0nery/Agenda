from django.shortcuts import render, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.http  import HttpResponse
# Create your views here.


def index(request):

    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 7)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {'contatos': contatos})

def ver_contato(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render(request, 'contatos/ver_contato.html', {'contato': contato})
def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'OCORREU UM ERRO!')
        redirect('index')
    cambo= Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(nome_completo=cambo).filter(nome_completo__icontains=termo)
    paginator = Paginator(contatos, 7)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {'contatos': contatos})
