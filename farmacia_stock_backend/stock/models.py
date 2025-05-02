from djongo import models
from bson.objectid import ObjectId

class Producto(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)  # ✅ usamos _id como primary_key
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Farmacia(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    ubicacion = models.JSONField()

    def __str__(self):
        return self.nombre

class Lote(models.Model):
    fecha_caducidad = models.DateField()
    cantidad = models.IntegerField()

    class Meta:
        abstract = True

class Inventario(models.Model):
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    minimo = models.IntegerField(default=0)
    lotes = models.JSONField()