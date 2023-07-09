from django.db import models

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=125)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural = "catergoriasProd"
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):

    nombre = models.CharField(max_length=125)
    precio = models.IntegerField(max_length=40)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="producto"
        verbose_name_plural = "productos"
    def __str__(self):
        return self.nombre

# Create your models here.
