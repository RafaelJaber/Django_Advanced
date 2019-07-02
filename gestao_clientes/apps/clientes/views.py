from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from gestao_clientes.apps.vendas.models import Sale
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
decorators = [login_required]


@login_required
def persons_list(request):
    persons = Person.objects.all()
    footer_message = 'Desenvolvimento web com Django 2.x'
    return render(request, 'person.html', {'persons': persons, 'footer_message': footer_message})


@login_required
def persons_list2(request, pk):
    context = {}
    context['footer_message'] = 'Desenvolvimento web com Django 2.x'
    person = Person.objects.filter(id=pk)
    template = 'clientes/person_detail.html'
    context['object'] = person
    context['now'] = timezone.now()
    context['sales'] = Sale.objects.filter(
        pessoa_id=pk
    )
    return render(request, template, context)


@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('Não autorizado')
    form = PersonForm(request.POST or None, request.FILES or None)
    footer_message = 'Desenvolvimento web com Django 2.x'

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form, 'footer_message': footer_message})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    footer_message = 'Desenvolvimento web com Django 2.x'

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form, 'footer_message': footer_message})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    footer_message = 'Desenvolvimento web com Django 2.x'
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person, 'footer_message': footer_message})


class PersonList(LoginRequiredMixin, ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        if not primeiro_acesso:
            context['message'] = 'Seja bem vindo ao seu primeiro acesso hoje'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'Já teve acesso'
        return context


class PersonDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'clientes.list_clients'
    permission_denied_message = 'Seu acesso não é autorizado'
    model = Person
    template_name = 'clientes/person_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['sales'] = Sale.objects.filter(
            person_id=self.object.id
        )

        return context


class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

    success_url = reverse_lazy('persons_list')


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

    success_url = reverse_lazy('persons_list')


class PersonDelete(DeleteView):
    model = Person

    success_url = reverse_lazy('persons_list')


