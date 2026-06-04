from django.shortcuts import render
from .models import Productbase
from django.contrib.auth.decorators import login_required
from user_app.urls import login_page

# Create your views here.

@login_required(login_url='login_page')
def products_page(r):
    products = Productbase.objects.all()
    context = {'products': products}
    return render(r, 'products_page.html', context)

