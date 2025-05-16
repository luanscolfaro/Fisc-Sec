from rest_framework.routers import DefaultRouter
from home.api.viewsets import PaginaInicialViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'home', PaginaInicialViewSet, basename='home')

urlpatterns = [
    path('', include(router.urls)),
]
