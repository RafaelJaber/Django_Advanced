from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView


# TODO: Refatorar para usar threads assim que possivel
def home(request):
    return render(request, 'home.html')


# FIXME: Corrigir bug ....
def my_logout(request):
    logout(request)
    return redirect('home')


class HomePageTemplateView(TemplateView):
    template_name = "home2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Olá está é uma linda variável que quer te atolar'
        return context
