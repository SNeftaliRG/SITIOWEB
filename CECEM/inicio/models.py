from django.db import models

# Create your models here.
class Taller(models.Model):
    # Nombre del taller
    nombre = models.CharField(max_length=100)
    
    # Imagen del taller
    imagen = models.ImageField(upload_to='talleres/', null=True, blank=True)
    
    # Días en los que se imparte el taller
    dias = models.CharField(max_length=200)  # Ejemplo: "Lunes, Miércoles, Viernes"
    
    # Horario del taller
    horario = models.CharField(max_length=100)  # Ejemplo: "9:00 AM - 11:00 AM"
    
    # Instructor del taller
    instructor = models.CharField(max_length=100)  # Nombre del instructor
    
    # Información de contacto
    contacto = models.CharField(max_length=100)  # Ejemplo: "Telefono: 123-456-7890"
    
    # Fecha de creación del taller (opcional)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre