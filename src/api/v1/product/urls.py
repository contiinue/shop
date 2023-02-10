from django.urls import path, include
from .router import router


urlpatterns = [path("session/", include(router.urls))]
