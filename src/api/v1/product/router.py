from rest_framework.routers import DefaultRouter

from .views import CreateSessionView

router = DefaultRouter()

router.register("", CreateSessionView, basename="create-session")
