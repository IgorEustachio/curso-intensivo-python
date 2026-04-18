from django.db import models

# Create your models here.

class Topic(models.Model):
    #um tópico que o usuário está aprendendo
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self): 
    #método especial, trata a string quando voce da um print, por exemplo
    return self.text