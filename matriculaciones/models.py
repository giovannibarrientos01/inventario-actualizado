from django.db import models

# Create your models here.
from django.db import models

class Matricula(models.Model):
    # Información básica del estudiante
    estudiante = models.CharField(max_length=200)
    codigo_estudiante = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20)
    email = models.EmailField()
    
    # Información académica
    carrera = models.CharField(max_length=200)
    semestre = models.IntegerField()
    año_academico = models.IntegerField()
    
    # Estado y pago
    estado = models.CharField(
        max_length=20,
        choices=[
            ('PENDIENTE', 'Pendiente'),
            ('APROBADA', 'Aprobada'),
            ('RECHAZADA', 'Rechazada')
        ],
        default='PENDIENTE'
    )
    pagado = models.BooleanField(default=False)
    
    # Fechas
    fecha_matricula = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.codigo_estudiante} - {self.estudiante}"
    