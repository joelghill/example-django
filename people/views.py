from django.http import response
from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from django.template.response import SimpleTemplateResponse
from first_app.views import hello_world
from people.models import Person
from people.forms import FirstNameForm


class PersonInfoMixin:

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        person = Person.objects.get(pk=pk)
        context  = {
            'person': person
        }
        return context


class AllEmails(View):

    def get(self, request):
        emails = Person.objects.all().values_list('email', flat=True)
        return response.JsonResponse(data=list(emails), safe=False)

class PersonInfo(TemplateView):

    template_name = 'person.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        person = Person.objects.get(pk=pk)
        context['person'] = person

        if self.request.method == 'POST':
            context['form'] = FirstNameForm(self.request.POST)
        else:
            context['form'] = FirstNameForm()

        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        person = context['person']
        form = context['form']
        if form.is_valid():
            person.first_name = form.cleaned_data['first_name']
            person.save()
            return redirect('people-list')
        else:
            return render(request, self.template_name, context=context)




class PersonListView(ListView):
    template_name = 'person_list.html'
    model = Person