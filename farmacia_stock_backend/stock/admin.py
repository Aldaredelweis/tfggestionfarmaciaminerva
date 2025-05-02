from django.contrib import admin
from .models import Producto, Farmacia, Inventario  # Importar los modelos

admin.site.register(Producto)   # Registrar el modelo de Producto
admin.site.register(Farmacia)   # Registrar el modelo de Farmacia
admin.site.register(Inventario) # Registrar el modelo de Inventario
