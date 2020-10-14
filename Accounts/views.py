from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm


# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'Accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all();
    return render(request, 'Accounts/products.html', {'products': products})


def customer(request, req_id):
    customer = Customer.objects.get(id=req_id)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'Accounts/customer.html', context)


def create_order(request):
    order_form = OrderForm()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('/')

    context = {'form': order_form}
    return render(request, 'Accounts/order_now.html', context)


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    update_form = OrderForm(instance=order)

    if request.method == 'POST':
        update_form = OrderForm(request.POST, instance=order)
        if update_form.is_valid():
            update_form.save()
            return redirect('/')

    context = {'form': update_form}
    return render(request, 'Accounts/order_now.html', context)


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'order': order}
    return render(request, 'Accounts/delete.html', context)
