from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import carName, Manufacturer
from .forms import carNameForm, ManufacturerForm
from django.shortcuts import render


def cardetails(request, num=None):
    instance = carName.objects.get(id = num)
    context = {
     "car" : instance,}
    return render(request,"carview.html",context) 


class carNameListView(ListView):
    model = carName


class carNameCreateView(CreateView):
    model = carName
    form_class = carNameForm


class carNameDetailView(DetailView):
    model = carName


class carNameUpdateView(UpdateView):
    model = carName
    form_class = carNameForm


class ManufacturerListView(ListView):
    model = Manufacturer


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm


class ManufacturerDetailView(DetailView):
    model = Manufacturer


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm

