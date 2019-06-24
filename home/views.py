from django.shortcuts import render, redirect
from django.contrib.auth import logout


# TODO: Refatorar para usar threads assim que possivel
def home(request):
    return render(request, 'home.html')


# FIXME: Corrigir bug ....
def my_logout(request):
    logout(request)
    return redirect('home')
