from django.urls import path, include
from .views import ItemView

urlpatterns = [path("item/<int:pk>", ItemView.as_view())]
