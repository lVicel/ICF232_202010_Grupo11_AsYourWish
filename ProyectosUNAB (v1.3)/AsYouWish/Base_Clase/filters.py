import django_filters
from .models import Klase

Locales_Disponibles=[('Casa Matriz','Casa Matriz'),('Bellavista','Bellavista'),('Providencia','Providencia'),('La Florida','La Florida'),]


class Filtro_Clases(django_filters.FilterSet):
    NombreClas = django_filters.CharFilter(label='Nombre Clase')
    Local = django_filters.ChoiceFilter(label='Local', choices=Locales_Disponibles)
    class Meta:
        model = Klase
        fields = ('NombreClas', 'Local','Profesor')

