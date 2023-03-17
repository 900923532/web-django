from django.db import models
# Create your models here.

class Servicio (models.Model):
    Titulo = models.CharField(max_length=50)
    Contenido = models.CharField( max_length=50)
    Imagen = models.ImageField(upload_to='servicios', null = True, blank= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

class Meta:
    verbose_name = 'servicio'
    verbose_name_plural = 'servicio'
    def __str__(self) -> str:
        return self.Titulo