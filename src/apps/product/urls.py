from django.urls import include, path

from .views import CancelPayment, ItemView, OrderView, SuccessPayment

urlpatterns = [
    path("item/<int:pk>", ItemView.as_view()),
    path("order/<int:pk>", OrderView.as_view()),
    path("cancel/", CancelPayment.as_view(), name="cansel-payment"),
    path("success/", SuccessPayment.as_view(), name="success-payment"),
]
