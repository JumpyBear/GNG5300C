from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
# Create your views here.
from django.http import HttpResponse
from django.views import View
from .forms import InputForm
from .forms import GeeksForm
from .forms import MyForm
from .models import GeeksModel
import datetime
from django.forms import formset_factory


def index(request):
    return HttpResponse("Hello Geeks")


def home_view(request):
    context={}
    form = GeeksForm(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form'] = form
    return render(request, "home.html", context)


def formset_view(request):
    context = {}

    # creating a formset
    GeeksFormSet = formset_factory(MyForm, extra=3)
    formset = GeeksFormSet(request.POST or None)

    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)

    # Add the formset to context dictionary
    context['formset'] = formset
    return render(request, "home.html", context)


def model_view(request):
    context = {}

    # creating a formset
    geeksFormSet = formset_factory(GeeksForm, fields=['title', 'description'], extra=2)
    formset = geeksFormSet(request.POST or None)

    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)

    # Add the formset to context dictionary
    context['formset'] = formset
    return render(request, "home.html", context)


def geeks_view(request):
    context = {
        "data": "CFZ is the best!",
        "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render(request, "projectApp.html", context)


# create a function
def my_view(request):
    # date and time
    now = datetime.datetime.now()
    # convert to string
    html = 'Time is {}'.format(now)
    # return response
    return HttpResponse(html)


def list_view(request):
    context = {}
    context['dataset'] = GeeksModel.objects.all()
    return render(request, "list_view.html", context)


def create_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def detail_view(request, id):
    context = {}

    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id=id)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id=id)

    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    if request.method == 'POST':
        obj.delete()
        # redirect to home page
        return HttpResponseRedirect('/')

    return render(request, "delete_view.html", context)


class MyView(View):
    def get(self, request):
        return HttpResponse('result')


class GeeksCreate(CreateView):
    model = GeeksModel
    fields = ['title', 'description']
    success_url = '/'


class GeeksList(ListView):
    model = GeeksModel


class GeeksDetailView(DetailView):
    model = GeeksModel


class GeeksUpdateView(UpdateView):
    model = GeeksModel
    fields = ['title', 'description']
    # url to redirect after successfully
    # updating details
    success_url = '/'


class GeeksDeleteView(DeleteView):
    model = GeeksModel
    success_url = '/'


class GeeksFormView(FormView):
    form_class = GeeksForm
    template_name = "projectApp/geeksmodel_form.html"
    success_url = '/thanks/'

