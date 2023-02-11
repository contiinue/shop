from django import forms

from .models import Currency, Discount, Item, Order, Tax


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = "__all__"


class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = "__all__"


class CurrencyFormAdmin(forms.ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"


class CurrencyForm(forms.ModelForm):
    employee_id = forms.ModelChoiceField(
        label="Изменить валюту",
        widget=forms.Select(attrs={"class": "select_current", "id": "to_current"}),
        queryset=Currency.objects.all(),
    )

    class Meta:
        model = Currency
        fields = ("employee_id",)
