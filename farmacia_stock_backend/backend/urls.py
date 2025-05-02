from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stock.views import ProductoViewSet, FarmaciaViewSet, InventarioViewSet, home  # ✅ Importa home correctamente

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'farmacias', FarmaciaViewSet)
router.register(r'inventarios', InventarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API REST de Django
    path('', home, name='home'),  # Página de inicio
]
