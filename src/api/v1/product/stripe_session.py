from dataclasses import dataclass

import stripe
from django.urls import reverse_lazy

from config.settings import BASE_URL, STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


@dataclass
class PaymentData:
    count_month: int
    price: int


def create_session(
    amount: int, currency: str, name_product: str, quantity: int = 1
) -> stripe.checkout.Session:
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": currency,
                    "unit_amount": int(amount) * 100,
                    "product_data": {
                        "name": name_product,
                    },
                },
                "quantity": quantity,
            },
        ],
        mode="payment",
        success_url=BASE_URL + reverse_lazy("success-payment"),
        cancel_url=BASE_URL + reverse_lazy("cansel-payment"),
    )
    return checkout_session
