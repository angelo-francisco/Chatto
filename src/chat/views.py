from django.shortcuts import render


def chatHome(request):
    return render(request, "pages/chat.html")
