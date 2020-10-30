import django_filters
from .models import Alumno

class Filtro_Alumno(django_filters.FilterSet):
    RUT = django_filters.CharFilter(label='RUT')
    Nombre = django_filters.CharFilter(label='Nombre')
    Genero = django_filters.CharFilter(label='Genero')
    class Meta:
        model = Alumno
        fields = ('RUT', 'Nombre', 'Genero')