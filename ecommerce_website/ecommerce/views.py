import datetime
from django.shortcuts import redirect, render, get_list_or_404, render_to_response
from ecommerce.models import *

# Create your views here.

def index(request):
    """
    This view is called when the product list screen (/ ec / list /) is called.
    Return product information
    """

    products = get_list_or_404(Product)

    # Define a List that stores cart information in the session.
    if not request.session.has_key('cart'):
        request.session['cart'] = list()

    response = render(request, 'product_list.html', {'products': products})

    return response

def cart_add(request, product_id):
    """
    It is a view that is called when you add any product to the cart.
     Add the product ID of any product to the cart (session).
    """

    #   Add a product to your cart (session).
    if not request.session.has_key('cart'):
        request.session['cart'] = list()
    cart = request.session['cart']
    cart.append(product_id)
    request.session['cart'] = cart

    products = get_list_or_404(Product)

    response = redirect('/ec/list/', {'products': products})

    return response

def cart_delete(request, product_id):
    """
    This is a view that is called when you delete any item in the cart.
     Delete the product ID of any product from the cart (session).
    """

    #   Removes the specified product from the cart (session).
    if not request.session.has_key('cart'):
        request.session['cart'] = list()
    cart = request.session['cart']
    #   Delete all objects with the specified ID if the same product is in multiple lists
    cart = [item for item in cart if item is not str(product_id)]
    request.session['cart'] = cart

    products = get_list_or_404(Product)

    response = redirect('/ec/list/', {'products': products})

    return response


def cart_reset(request):
    """
    This is the view that will be executed if the cart is empty but clicked.
     Empty the contents of the cart (session).
    """

    #   Remove all products from your cart (session).
    if not request.session.has_key('cart'):
        request.session['cart'] = list()
    del request.session['cart']

    products = get_list_or_404(Product)

    response = redirect('/ec/list/', {'products': products})

    return response

def cart_list(request):
    """
    This view is executed when the page displaying the contents of the cart is displayed.
     Product information in the cart is returned.
    """

    #   Acquire the product ID in the cart (session).
    if not request.session.has_key('cart'):
        request.session['cart'] = list()
    cart = request.session['cart']

    #   Get product information in the cart
    products = Product.objects.filter(id__in=cart)

    return render(request, 'cart_list.html', {'products': products})

def order(request):
    """
   This view is executed when the order screen is displayed.
     Product information and payment method in the cart and return the order screen.
    """

    #   Acquire the product ID in the cart (session).
    if not request.session.has_key('cart'):
        request.session['cart'] = list()
    cart = request.session['cart']

    #   Get product information in the cart
    products = Product.objects.filter(id__in=cart)

    #   Get the payment method.
    payments = get_list_or_404(Payment)

    return render(request, 'order.html', {'products': products, 'payments': payments})

def order_execute(request):
    """
   It is a view that is executed when POSTed from the order screen.
     Save customer information and save ordered product information.
    """

    #   Save the sent customer information.
    customer = Customer(first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        postal_code=request.POST['postal_code'],
                        prefecture=request.POST['prefecture'],
                        city=request.POST['city'],
                        street1=request.POST['street1'],
                        street2 =request.POST['street2'],
                        tel=request.POST['tel'],
                        email=request.POST['email'])
    customer.save()

    #   Get Payment object.
    payment = Payment.objects.get(id=int(request.POST['payment']))

    #   Save order information.
    order = Order(customer=customer, payment=payment)
    order.save()

    #   Acquire the product ID in the cart (session)
    if not request.session.has_key('cart'):
        request.session['cart'] = list()
    cart = request.session['cart']

    #   Get product information in the cart
    products = Product.objects.filter(id__in=cart)

    for product in products:
        order_product = Order_Product(order=order, product=product, count=1, price=product.price)
        order_product.save()

    #   Redirect to the order complete screen.
    return redirect('/ec/order_complete/')

def order_complete(request):
    """
    It is a view that is executed when the order is completed.
     Returns the order complete screen.
    """

    response = render_to_response('order_complete.html')

    #   Delete the contents of the cart.
    if request.session.has_key('cart'):
        del request.session['cart']
    return response
