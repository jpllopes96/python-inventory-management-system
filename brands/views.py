from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from . import models, forms


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'  # object will be send to template

    #  overwrite the get to filter by name
    def get_queryset(self):
        queryset = super().get_queryset()  # return all registers
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class BrandCreateView(CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDetailView(DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'
    context_object_name = 'brand'
