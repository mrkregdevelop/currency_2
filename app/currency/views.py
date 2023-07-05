from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView,
    DeleteView, TemplateView
)
from django.urls import reverse_lazy

from currency.forms import RateForm, SourceForm
from currency.models import Rate


class RateListView(ListView):
    queryset = Rate.objects.all()
    # template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')


class IndexView(TemplateView):
    template_name = 'index.html'
