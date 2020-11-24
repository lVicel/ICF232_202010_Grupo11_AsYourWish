import django_filters
from .models import Evento
Locales_Disponibles=[('Casa Matriz','Casa Matriz'),('Bellavista','Bellavista'),('Providencia','Providencia'),('La Florida','La Florida'),]


class Filtro_Event(django_filters.FilterSet):
    NombreEvent=django_filters.CharFilter(label='Nombre Evento')
    LocalAdmin=django_filters.ChoiceFilter(label='Local Encargado', choices=Locales_Disponibles)
    class Meta:
        model = Evento
        fields = ('NombreEvent','LocalAdmin')

