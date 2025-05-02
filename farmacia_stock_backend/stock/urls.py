from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet, FarmaciaViewSet, InventarioViewSet, home

# 🔥 Creamos un router
router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'farmacias', FarmaciaViewSet)
router.register(r'inventarios', InventarioViewSet)

urlpatterns = [
    path('', home, name='home'),  # ruta de inicio
    path('api/', include(router.urls)),  # ✅ incluimos las rutas de la API
]
