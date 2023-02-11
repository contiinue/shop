from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .forms import CurrencyFormAdmin, DiscountForm, ItemForm, OrderForm, TaxForm
from .models import Currency, Discount, Item, Order, Tax


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
