from django.shortcuts import render
from random import randint
import requests
import datetime


def chatHome(request):
    rq = requests.get('https://gerador-nomes.wolan.net/apelidos/').json()
    request.session['username'] = rq[randint(0, 9)]
    openin = datetime.datetime.now()
    return render(request, "pages/chat.html", {'openin': openin})
