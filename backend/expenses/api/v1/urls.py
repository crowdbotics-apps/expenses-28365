from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ExpenseViewSet

router = DefaultRouter()
router.register("expense", ExpenseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
