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
    template_name = ''


class SuccessPayment(TemplateView):
    template_name = 'product/success-payment.html'


class CancelPayment(TemplateView):
    template_name = 'product/cancel-payment.html'
