from rest_framework import serializers
from .models import Producto, Farmacia, Inventario
from bson.decimal128 import Decimal128

class ProductoSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    precio = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = str(instance._id) if hasattr(instance, '_id') else None
        return rep

    def get_precio(self, obj):
        try:
            if isinstance(obj.precio, Decimal128):
                return float(obj.precio.to_decimal())
            return float(obj.precio) if obj.precio is not None else None
        except Exception as e:
            print("⚠️ Error en precio:", e)
            return None

    def validate_precio(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError("El precio debe ser un valor positivo.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value

# ✅ AÑADIMOS LAS DOS CLASES QUE FALTAN:

class FarmaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmacia
        fields = ['id', 'nombre', 'direccion', 'ubicacion']

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'farmacia', 'producto', 'cantidad', 'minimo', 'lotes']
        depth = 1






