import django_filters
from .models import Alumno
product_Genero= [('Hombre','Hombre'),('Mujer','Mujer'),]

class Filtro_Alumno(django_filters.FilterSet):
    RUT = django_filters.CharFilter(label='RUT')
    Nombre = django_filters.CharFilter(label='Nombre')
    Genero = django_filters.ChoiceFilter(label='Genero', choices=product_Genero)
    class Meta:
        model = Alumno
        fields = ('RUT', 'Nombre', 'Genero')