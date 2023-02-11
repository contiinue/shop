from django.urls import include, path

from .router import router

urlpatterns = [path("session/", include(router.urls))]
