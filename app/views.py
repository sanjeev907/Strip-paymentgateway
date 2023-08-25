# app_name/views.py
from django.shortcuts import render
import stripe
from django.http import HttpResponse
from django.conf import settings

def payment_view(request):
    if request.method == 'POST':
        # Process the payment using the Stripe API
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST.get('stripeToken')
        try:
            charge =  stripe.PaymentIntent.create(
                    amount=500,
                    currency="gbp",
                    payment_method="pm_card_visa",
                    source=token,
                    )
                
            
            # Handle successful payment
            return HttpResponse(request, 'Payment succesful')
        except stripe.error.CardError as e:
            # Handle card errors
            return HttpResponse(request, 'payment failed', {'error_msg': str(e)})
    
    return render(request, 'index.html')


# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
# import stripe
# stripe.api_key = "sk_test_tR3PYbcVNZZ796tH88S4VQ2u"

# stripe.PaymentIntent.create(
#   amount=500,
#   currency="gbp",
#   payment_method="pm_card_visa",
# )
