from django.shortcuts import render
from .models import Contato
from django.core.paginator import Paginator
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
