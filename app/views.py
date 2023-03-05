from django.shortcuts import render
from .models import Product
from .forms import OrderForm

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)

def form(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'app/form.html', {'form': form})

def success(request):
    return render(request, 'app/success.html')