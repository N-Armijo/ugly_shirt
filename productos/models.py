from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Polera(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.precio<2000:
            raise ValidationError({'precio':'El precio no puede ser menor a 2000.'})
        
    def __str__(self) -> str:
        return self.nombre