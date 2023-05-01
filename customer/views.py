from django.shortcuts import render
from .models import Customer
from . import options

# Create your views here.



def customer(request):
    customers = Customer.objects.all()
    context = {}
    filter = 'ALL'
    sort_by = 'name'
    sort_order = 'ASC'

    if(request.method == 'POST'):

        filter = request.POST['filter'] 
        if(filter=='ALL'):
            customers = Customer.objects.all()
        else:  
            customers = Customer.objects.filter(type=filter)

        sort_by = request.POST['sort_by']
        sort_order = request.POST['sort_order']
        if(sort_order=='ASC'):
            customers = customers.order_by(sort_by)
        else:
            customers = customers.order_by('-'+sort_by)
    context = {'customers': customers, 'options': options.STATUS_CHOICES, 'filter': filter,
            'sort_by': sort_by,
            'sort_order': sort_order,}
    return render(request, 'customer.html', context)