from django.urls import path, include
from .views import ItemView, SuccessPayment, CancelPayment

urlpatterns = [
    path("item/<int:pk>", ItemView.as_view()),
    path('cancel/', CancelPayment.as_view(), name='cansel-payment'),
    path('success/', SuccessPayment.as_view(), name='success-payment')
]
