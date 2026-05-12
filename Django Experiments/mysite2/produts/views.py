from django.shortcuts import render

# Create your views here.
def allproduct(request):
    return render(request, 'product_home.html')