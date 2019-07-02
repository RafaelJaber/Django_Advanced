from django.shortcuts import render, redirect, HttpResponse, render_to_response
from django.contrib.auth import logout
from django.views.generic.base import TemplateView, View


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


class MyView(View):

    def get(self, request, *args, **kwargs):
        response = render_to_response('home3.html')
        response.set_cookie('color', 'blue', max_age=1000)
        mycookie = request.COOKIES.get('color')
        print(mycookie)
        return response

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST Maluco')
