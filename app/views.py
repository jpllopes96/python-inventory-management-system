from django.shortcuts import render
from . import metrics

def home(request):
    # product_metrics = {
    #     'total_quantity': 1000,
    #     'total_cost_price': 1000000,
    #     'total_selling_price': 3000000,
    #     'total_profit': 200000
    # }
    # product_metrics = metrics.get_product_metrics()
    context = {
        'product_metrics': metrics.get_product_metrics()
    }
    return render(request, 'home.html', context)