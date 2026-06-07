from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    # a página inicial para o registro de aprendizagem
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    #mostra um único tópico e todas as suas entradas
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)