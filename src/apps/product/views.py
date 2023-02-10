from django.forms import model_to_dict
from django.views.generic import DetailView

from config.settings import STRIPE_PUBLIC_KEY
from .forms import CurrencyForm
from .models import Item


class ItemView(DetailView):
    model = Item
    template_name = "product/payment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["currency_form"] = CurrencyForm()
        context['STRIPE_PUBLIC_KEY'] = STRIPE_PUBLIC_KEY
        return context
