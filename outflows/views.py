from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from . import models, forms


class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'  # object will be send to template
    paginate_by = 10

    #  overwrite the get to filter by product name
    def get_queryset(self):
        queryset = super().get_queryset()  # return all registers
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')


class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
    context_object_name = 'outflow'
