from django.contrib import admin
from django.urls import path, include
from demanda.api.router import router
from usuario.api.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(usuario_router.urls)),
    path('api/home/', include('home.api.router')),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
