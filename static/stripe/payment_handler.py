import stripe
stripe.api_key = "STRIPE_KEY"

def create_payment_intent():
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=1000,  # amount in cents
            currency="eur",
            payment_method_types=["card", "paypal"]
        )
        return payment_intent
    except Exception as e:
        return {"error": str(e)}