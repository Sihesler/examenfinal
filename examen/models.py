from django.db import models
from django.contrib import admin

# Create your models here.
class Materia(models.Model):
    curso     =  models.CharField(max_length=100)
    profesor  =  models.CharField(max_length=100)
    hora      =  models.CharField(max_length=100)
    def __str__(self):
        return self.curso


class Carrera(models.Model):
    nombre    = models.CharField(max_length=100)
    seccion   = models.CharField(max_length=100)
    alumno    = models.CharField(max_length=100)
    materias  = models.ManyToManyField(Materia, through='Asignacion')
    def __str__(self):
        return self.nombre


class Asignacion(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nota = models.IntegerField()


class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


class CarreraAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
