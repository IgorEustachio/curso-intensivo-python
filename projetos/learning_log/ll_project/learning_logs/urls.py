# define padrões de URL para learning_logs

from django.urls import path

from . import views #o . importa do mesmo diretório que o módulo atual

app_name = 'learning_logs'

urlpatterns = [
    #página inicial
    path('', views.index, name='index'), #views. se refere ao arquivo views
    path('topics/', views.topics, name='topics'), 
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]