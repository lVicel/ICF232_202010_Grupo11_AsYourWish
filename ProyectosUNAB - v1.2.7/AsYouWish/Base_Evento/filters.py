import django_filters
from .models import Evento

class Filtro_Event(django_filters.FilterSet):
    NombreEvent=django_filters.CharFilter(label='Nombre Evento')
    class Meta:
        model = Evento
        fields = ('NombreEvent',)

