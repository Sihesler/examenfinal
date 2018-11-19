from django.contrib import admin
from examen.models import Materia, MateriaAdmin, Carrera, CarreraAdmin


admin.site.register(Materia, MateriaAdmin)
admin.site.register(Carrera, CarreraAdmin)
