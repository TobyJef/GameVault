from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_basket(request):
    """ A view that renders the basket contents page """
    
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of a specific product to the basket  """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('bakset', {})



    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else: 
        basket[item_id] = quantity

    request.session['basket'] = bakset
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust product quantity to the specified amount  """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('bakset', {})

    if quantity > 0:
        basket[item_id] = quantity
    else: 
        basket.pop(item_id)

    request.session['basket'] = bakset
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove item from the shopping basket """

    try:
        basket = request.session.get('bakset', {})

        if quantity > 0:
            basket[item_id] = quantity
        else: 
            basket.pop(item_id)

        request.session['basket'] = bakset
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(staus=500)


    