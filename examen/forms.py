from django import forms
from .models import Materia, Carrera

#todos los campos de Pelicula
class CarreraForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Carrera
        fields = ('nombre', 'seccion', 'alumno', 'materias')

        def __init__ (self, *args, **kwargs):
            super(CarreraForm, self).__init__(*args, **kwargs)

            #En este caso vamos a usar el widget checkbox multiseleccionable.

            self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()

            #Podemos usar un texto de ayuda en el widget

            self.fields["materias"].help_text = "Ingrese las materias"

            #En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

            self.fields["materias"].queryset = Materia.objects.all()



class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('curso', 'profesor', 'hora')
