from rest_framework import viewsets
from .models import Producto, Farmacia, Inventario
from .serializers import ProductoSerializer, FarmaciaSerializer, InventarioSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from bson import ObjectId  # 👈 ya no necesitamos Decimal128

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = '_id'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        raw_id = self.kwargs.get(self.lookup_field) or self.kwargs.get('pk')

        try:
            object_id = ObjectId(raw_id)  # ✅ convertimos a ObjectId
        except Exception as e:
            print(f"⚠️ Error al convertir _id: {e}")
            raise

        filter_kwargs = {self.lookup_field: object_id}
        return get_object_or_404(queryset, **filter_kwargs)

    def perform_create(self, serializer):
        producto = serializer.save()  # guarda los otros campos
        precio_valor = self.request.data.get('precio')
        if precio_valor is not None:
            try:
                producto.precio = float(str(precio_valor))
                producto.save()  # guardamos manualmente el precio como Decimal128
            except Exception as e:
                print(f"⚠️ Error al asignar precio: {e}")

    def perform_update(self, serializer):
        producto = serializer.save()
        precio_valor = self.request.data.get('precio')
        if precio_valor is not None:
            try:
                producto.precio = float(str(precio_valor))
                producto.save()
            except Exception as e:
                print(f"⚠️ Error al actualizar precio: {e}")

class FarmaciaViewSet(viewsets.ModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

def home(request):
    return HttpResponse("¡Django con MongoDB funcionando correctamente! 🚀")


