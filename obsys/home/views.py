from django.shortcuts import render, redirect
from .models import Tiffin, ColdDrink

def homepage(request):
    tiffins = Tiffin.objects.all()  
    return render(request, 'homepage.html', {'tiffins': tiffins})

def cold_drinks_page(request):
    cold_drinks = ColdDrink.objects.all()  
    return render(request, 'cold_drinks.html', {'cold_drinks': cold_drinks})
 
def cart_view(request):
    cart = request.session.get('cart', {})
    total_price = 0
    cart_items = [] 

    for item_key, item_details in cart.items():
        item_total = item_details['price'] * item_details['quantity']
        total_price += item_total
        cart_items.append({
            'name': item_details['name'],
            'quantity': item_details['quantity'],
            'price': item_details['price'],
            'total': item_total,  
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)
 
  
def add_to_cart(request, item_id, item_type):
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    item_key = None  # Initialize item_key to None

    if item_type == 'tiffin':
        try:
            tiffin = Tiffin.objects.get(id=item_id)
            item_key = f'tiffin_{item_id}'
        except Tiffin.DoesNotExist:
            return redirect('homepage')

    elif item_type == 'cold_drink':
        try:
            cold_drink = ColdDrink.objects.get(id=item_id)
            item_key = f'cold_drink_{item_id}'
        except ColdDrink.DoesNotExist:
            return redirect('homepage')

    # Ensure item_key is defined before proceeding
    if item_key:
        # Update cart with item
        if item_key in cart:
            cart[item_key]['quantity'] += quantity
        else:
            cart[item_key] = {
                'name': tiffin.name if item_type == 'tiffin' else cold_drink.name,
                'quantity': quantity,
                'price': tiffin.price if item_type == 'tiffin' else cold_drink.price,
            } 

        request.session['cart'] = cart
        
    # Redirect to the referring page
    return redirect(request.META.get('HTTP_REFERER', 'homepage'))


def pay_view(request):

    if 'cart' in request.session:
        del request.session['cart']  

    return render(request, 'payment_successful.html')  
 