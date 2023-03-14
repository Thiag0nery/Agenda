from django.db import models
from django.utils import timezone
# Create your models here.
class Contegoria(models.Model):
    nome = models.CharField(max_length=255)

    # Para exebir o nome da categoria na pagina admin, para não aparecer Object se utiliza-se essa função
    def __str__(self):
        return self.nome
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data = models.DateTimeField(default=timezone.now)
    descriacao = models.CharField(max_length=255, blank=True)
    contegoria = models.ForeignKey(Contegoria, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nome