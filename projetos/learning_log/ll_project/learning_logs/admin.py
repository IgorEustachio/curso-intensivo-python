from django.contrib import admin
from .models import Topic, Entry

# Register your models here.
#TEMOS QUE REGISTRAR TODO MODELO CRIADO AQUI, PARA APARECER NO SITE ADMIN
admin.site.register(Topic)
admin.site.register(Entry)
