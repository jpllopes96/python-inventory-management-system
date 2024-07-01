from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from . import models, forms


class InflowListView(ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'  # object will be send to template
    paginate_by = 10

    #  overwrite the get to filter by product name
    def get_queryset(self):
        queryset = super().get_queryset()  # return all registers
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')


class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'inflow'
