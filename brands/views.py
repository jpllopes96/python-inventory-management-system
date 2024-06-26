from django.views.generic import ListView
from . import models


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
