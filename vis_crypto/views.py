from django.shortcuts import render

def index(request):
    return render(request, "vis_crypto/base.html")
