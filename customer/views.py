from django.shortcuts import render
from .models import Customer
from . import options




def customer(request):
    customers = Customer.objects.all() # get all customers
    context = {} # create empty context dictionary
    filter = 'ALL' # default filter
    sort_by = 'name' # default sort_by
    sort_order = 'ASC' # default sort_order  

    if(request.method == 'POST'): # if form is submitted

        filter = request.POST['filter']  # get filter from form
        if(filter=='ALL'):
            customers = Customer.objects.all()
        else:  
            customers = Customer.objects.filter(type=filter) # filter customers by type

        sort_by = request.POST['sort_by'] # get sort_by from form
        sort_order = request.POST['sort_order']
        if(sort_order=='ASC'): # if sort_order is ASC
            customers = customers.order_by(sort_by)
        else:
            customers = customers.order_by('-'+sort_by) # if sort_order is DESC
    context = {'customers': customers, 'options': options.STATUS_CHOICES, 'filter': filter,
            'sort_by': sort_by,
            'sort_order': sort_order,} # create context dictionary
    return render(request, 'customer.html', context) # render customer.html with context dictionary