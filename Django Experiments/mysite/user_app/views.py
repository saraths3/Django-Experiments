from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products_app.models import Productbase
from user_app.models import Cart, CartItems

# Create your views here.
def login_page(r):
    if r.method == 'POST':
        uname = r.POST.get('username')
        upasswd = r.POST.get('password')
        user = authenticate(r, username = uname, password = upasswd)
        if user:
            login(r, user)
            return redirect('product_page')
        else:
            print('No user')
    return render(r, 'login_page.html')

def registration_page(r):
    if r.method == 'POST':
        uname = r.POST.get('username')
        email = r.POST.get('email')
        upasswd1 = r.POST.get('password1')
        upasswd2 = r.POST.get('password2')
        if upasswd1 != upasswd2:
            error_context1 = {'error': 'Enter the same passwords.'}
            return render(r, 'registration_page.html', error_context1)
        if User.objects.filter(username=uname).exists():
            error_context2 = {'error': 'Username already exists, try other names.'}
            return render(r, 'registration_page.html', error_context2)
        user = User.objects.create_user(username=uname, email=email, password=upasswd1)
        cart = Cart.objects.create(user=user)
        cart.save()
        return redirect('login_page')
    return render(r, 'registration_page.html')

def logout_page(r):
    logout(r)
    messages.success(r, 'Logout Successfull')
    return redirect(login_page)

@login_required(login_url='login_page')
def cart_page(r):
    user = r.user
    try:
        cart = Cart.objects.get(user=user)
        cart_items = CartItems.objects.filter(cart=cart)
    except Cart.DoesNotExist:
        cart_items = []
    
    total_price = 0
    total_quantity = 0
    for item in cart_items:
        total_price += float(item.product.price) * item.quantity
        total_quantity += item.quantity
    
    context = {
        'cart_items': cart_items,
        'total_price': f"{total_price:.2f}",
        'total_quantity': total_quantity
    }
    return render(r, 'cart_page.html', context)

@login_required(login_url='login_page')
def add_cart(r, pid):
    product = Productbase.objects.get(id=pid)
    user = r.user
    cart, created = Cart.objects.get_or_create(user=user)
    if r.method == 'POST':
        quantity = int(r.POST.get('quantity', 1))
        cart_item, item_created = CartItems.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        if not item_created:
            cart_item.quantity += quantity
            cart_item.save()
        return redirect('cart_page')
    return render(r, 'cart_page.html')

@login_required(login_url='login_page')
def delete_from_cart(r, item_id):
    try:
        cart_item = CartItems.objects.get(id=item_id)
        cart_item.delete()
        messages.success(r, 'Item removed from cart')
    except CartItems.DoesNotExist:
        messages.error(r, 'Item not found')
    return redirect('cart_page')

@login_required(login_url='login_page')
def update_quantity(r, item_id):
    try:
        cart_item = CartItems.objects.get(id=item_id)
        if r.method == 'POST':
            action = r.POST.get('action')
            if action == 'increase':
                cart_item.quantity += 1
            elif action == 'decrease':
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                else:
                    cart_item.delete()
                    messages.success(r, 'Item removed from cart')
                    return redirect('cart_page')
            cart_item.save()
            messages.success(r, 'Quantity updated')
    except CartItems.DoesNotExist:
        messages.error(r, 'Item not found')
    return redirect('cart_page')