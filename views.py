# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from extra_views import SearchableListMixin

from .models import {{ app_name|title }}
from .forms import {{ app_name|title }}Form


class {{ app_name|title }}List(SearchableListMixin, ListView):
    template_name = '{{ app_name }}/list.html'
    search_fields = []
    model = {{ app_name|title }}


class {{ app_name|title }}New(CreateView):
    model = {{ app_name|title }}
    template_name = '{{ app_name }}/new.html'
    form_class = {{ app_name|title }}Form
    success_url = reverse_lazy('{{ app_name }}:list')


class {{ app_name|title }}Update(UpdateView):
    model = {{ app_name|title }}
    template_name = '{{ app_name }}/update.html'
    form_class = {{ app_name|title }}Form
    success_url = reverse_lazy('{{ app_name }}:list')


class {{ app_name|title }}Delete(DeleteView):
    model = {{ app_name|title }}
    template_name = '{{ app_name }}/confirm_delete.html'
    success_url = reverse_lazy('{{ app_name }}:list')
