from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    basket = request.session.get('basket',{})
    if not basket:
        messages.error(request, "No items found in your basket")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q7GNXGHjt7sxbbVp3cfjQl6uuEFQq45HeGfFRwLxl3gn3eEqNZnuwMqzp7jBYExJenbAIeT7K5cZYnGjjoJYbWt00RBdPMnWl',
        'client_secret': 'test client secret',

    }

    return render(request, template, context)