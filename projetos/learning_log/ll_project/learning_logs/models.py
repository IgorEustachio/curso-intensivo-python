from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    #um tópico que o usuário está aprendendo
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
    #método especial, trata a string quando voce da um print, por exemplo
        return self.text

class Entry(models.Model): #herda do model base do Django
    #algo específico aprendido sobre um tópico
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #a variavel topic é uma instancia de ForeignKey. cada tópico recebe uma chave/ID. relaciona topic com entry
    #cascade significa que quando um tópico for deletado, tudo relacionado a ele com ForeignKey será excluído tbm

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: #dentro da classe entry. serve pro django usar entries(correto) ao invés de entrys(errado) quando for falar de mais de uma entry
        verbose_name_plural = 'entries'

    def __str__(self):
        #método especial. retorna uma string simples representando a entrada
        if len(self.text) > 50: 
            return f"{self.text[:50]}..."
        else:
            return self.text

