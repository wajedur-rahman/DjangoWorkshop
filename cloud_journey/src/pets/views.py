from django.shortcuts import render

# Create your views here.
#cloud_journey/src/pets/views.py
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from pets.models import Pets


class PetsListView(ListView):
    model = Pets

#cloud_journey/src/pets/views.py
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from pets.models import Pets


class PetsListView(ListView):
    model = Pets
    
class PetCreateView(CreateView):
    model = Pets
    fields = ["title", "description"]

#cloud_journey/src/pets/views.py
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from pets.models import Pets


class PetsListView(ListView):
    model = Pets
    

class PetCreateView(CreateView):
    model = Pets
    fields = ["title", "description"]
    

class PetUpdateView(UpdateView):
    model = Pets
    fields = ["title", "description"]

class PetDetailView(DetailView):
    model = Pets