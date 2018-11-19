from django.shortcuts import render
from django.contrib import messages
from .forms import CarreraForm
from examen.models import Materia, Carrera





def carrera_nueva(request):

    if request.method == "POST":

        formulario = CarreraForm(request.POST)

        if formulario.is_valid():

            carrera = Carrera.objects.create(nombre=formulario.cleaned_data['nombre'], seccion = formulario.cleaned_data['seccion'], alumno = formulario.cleaned_data['alumno'])

            for materia_id in request.POST.getlist('materias'):

                asignacion = Asignacion(materia_id=materia_id, carrera_id = carrera.id)

                asignacion.save()

            messages.add_message(request, messages.SUCCESS, 'Asignacion Guardada Exitosamente')

    else:

        formulario = CarreraForm()

    return render(request, 'examen/crear.html', {'formulario': formulario})
