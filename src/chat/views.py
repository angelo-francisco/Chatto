from django.shortcuts import render
from random import randint
import requests

def chatHome(request):
    rq = requests.get('https://gerador-nomes.wolan.net/apelidos/').json()
    request.session['username'] = rq[randint(0, 9)]

    return render(request, "pages/chat.html")
