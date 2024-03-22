from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from . models import Unit
from django.http.response import HttpResponse
import json

class UnitListView(ListView):
    queryset = Unit.objects.filter(is_active=True)
    template_name = "web/object_list.html"