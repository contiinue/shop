from django.db.models import Count, Sum, F
from django.views.generic import DetailView, TemplateView

from config.settings import STRIPE_PUBLIC_KEY
from .forms import CurrencyForm
from .models import Item, Order


class ItemView(DetailView):
    model = Item
    template_name = "product/payment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["currency_form"] = CurrencyForm()
        context["STRIPE_PUBLIC_KEY"] = STRIPE_PUBLIC_KEY
        return context


class OrderView(DetailView):
    model = Order
    template_name = "product/order.html"

    def get_queryset(self):
        return (
            Order.objects.select_related("discount", "tax")
            .filter(pk=self.kwargs["pk"])
            .annotate(
                quantity=Count("items"),
                amount=Sum(
                    F("items__price")
                    - (F("items__price") / 100 * F("discount__discount_percentage"))
                    - (F("items__price") / 100 * F("tax__tax_percentage"))
                ),
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["currency"] = "usd"
        context["currency_form"] = CurrencyForm()
        context["STRIPE_PUBLIC_KEY"] = STRIPE_PUBLIC_KEY
        return context


class SuccessPayment(TemplateView):
    template_name = "product/success-payment.html"


class CancelPayment(TemplateView):
    template_name = "product/cancel-payment.html"
