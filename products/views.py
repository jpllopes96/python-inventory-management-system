from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . import models, forms


class ProductListView(ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'  # object will be send to template
    paginate_by = 10

    #  overwrite the get to filter by product title
    def get_queryset(self):
        queryset = super().get_queryset()  # return all registers
        title = self.request.GET.get('title')

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset


class ProductCreateView(CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
