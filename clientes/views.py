from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Person, Produto, Venda
from .forms import PersonForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import View
from django.utils.decorators import method_decorator

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
    context['sales'] = Venda.objects.filter(
        pessoa_id=pk
    )
    return render(request, template, context)


@login_required
def persons_new(request):
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


class PersonList(ListView):
    model = Person


@method_decorator(login_required, name='dispatch')
class PersonDetail(DetailView):
    model = Person
    template_name = 'clientes/person_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['sales'] = Venda.objects.filter(
            pessoa_id=self.object.id
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


class ProductBulk(View):

    def get(self, request):
        products = ['banana', 'maçã', 'limão', 'Laranja', 'Pera', 'Melancia']
        list_products = []

        for product in products:
            p = Produto(descricao=product, preco=10)
            list_products.append(p)

        Produto.objects.bulk_create(list_products)
        return HttpResponse(request, 'Criado')

