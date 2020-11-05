import django_filters
from .models import Klase


class Filtro_Clases(django_filters.FilterSet):
    NombreClas = django_filters.CharFilter(label='Nombre Clase')
    Local = django_filters.CharFilter(label='Local')
    ClassInicio = django_filters.CharFilter(label='Horario Inicio')
    ClassTermino = django_filters.CharFilter(label='Horario Termino')
    class Meta:
        model = Klase
        fields = ('NombreClas', 'Local', 'ClassInicio', 'ClassTermino','Profesor')

