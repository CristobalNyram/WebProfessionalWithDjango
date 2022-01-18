
from django.http import HttpResponse
def saludo(request):
    return HttpResponse("<h1>Saludo</h2><hr> <br> <p>Soy una vista con HTML</p>  <a href='http://127.0.0.1:8000/hablar'>Ve a hablar</a> ")

def despedida(request):
    return HttpResponse("<h1>Despedida </h2><hr> <br> <p>Soy una vista con HTML</p> <a href='http://127.0.0.1:8000/saludo'>Ve a saludo</a> ")   

def hablar(request):
    return HttpResponse("<h1>Hablar </h2><hr> <br> <p>Soy una vista con HTML</p> <a href='http://127.0.0.1:8000/despedida'>Ve a despedida</a> ")     