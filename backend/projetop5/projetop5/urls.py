from django.contrib import admin
from django.urls import path, include
from demanda.api.router import router
from usuario.api.router import router as usuario_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(usuario_router.urls)), 
]
