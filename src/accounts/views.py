from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Customer, Order, Product
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter


# Register Page View
def registerPage(request):
    '''
    Sets up a view for new user registration.
    '''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


# Login Page View
def loginPage(request):
    '''
    Sets up a login page view.
    '''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


# Logout User View
def logoutUser(request):
    '''
    Sets up a view for logout.
    '''
    logout(request)
    return redirect('login')


# Home Page View
@login_required(login_url='login')
def home(request):
    '''
    Sets up a view for home page.
    '''
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
               'orders': orders,
               'customers': customers,
               'total_orders': total_orders,
               'delivered': delivered,
               'pending': pending
              }

    return render(request, 'accounts/dashboard.html', context)

# Products Page View
@login_required(login_url='login')
def products(request):
    '''
    Sets up a view for product page.
    '''
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})

# Customer Page View
@login_required(login_url='login')
def customer(request, pk_test):
    '''
    Sets up a view for a particular customer.
    '''
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter
    }
    return render(request, 'accounts/customer.html', context)

# Create Order View
@login_required(login_url='login')
def createOrder(request, pk):
    '''
    Sets up a view for creating new orders.
    '''
    OrderFormSet = inlineformset_factory(
                       Customer,
                       Order,
                       fields=('product', 'status'),
                       extra=2
                   )
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'accounts/order_form.html', context)

# Update Order View
@login_required(login_url='login')
def updateOrder(request, pk):
    '''
    Sets up a view for updating an order.
    '''
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

# Delete Order View
@login_required(login_url='login')
def deleteOrder(request, pk):
    '''
    Sets up a view to delete an order.
    '''
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
