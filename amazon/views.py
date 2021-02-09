from django.shortcuts import render, redirect
from .price_tracker import track_price
from django.contrib import messages



# Create your views here.
def price_tracker(request):
    """
    Track a particular product price.
    """
    if request.method == "POST":
        url = request.POST['url']
        email = request.POST['email']
        expected_price = request.POST['price']
        title, price, status = track_price(url, email, expected_price)
        if price is not None:
            messages.info(request, f'Product "{title}". You will be notified '
                                   f'if the price below ${expected_price}.')
        else:
            messages.info(request, f'Price not found for the product: "{title}"')
        return redirect('amazon:amazon_price_tracker')

    return render(request, 'amazon/amazon.html')
