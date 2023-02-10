from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Item, Order, Discount, Tax, Currency
from .forms import ItemForm, OrderForm, DiscountForm, TaxForm, CurrencyFormAdmin


@admin.register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ("name", "price")
    form = ItemForm


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ("discount",)
    form = OrderForm


@admin.register(Discount)
class DiscountAdmin(ModelAdmin):
    list_display = ("discount_percentage",)
    form = DiscountForm


@admin.register(Tax)
class TaxAdmin(ModelAdmin):
    list_display = ("tax_name", "tax_percentage")
    form = TaxForm


@admin.register(Currency)
class TaxAdmin(ModelAdmin):
    list_display = ("currency_name",)
    form = CurrencyFormAdmin
