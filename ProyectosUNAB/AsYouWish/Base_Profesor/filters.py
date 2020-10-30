import django_filters
from .models import Profesor

class Filtro_Profesor(django_filters.FilterSet):
    RUTprof = django_filters.CharFilter(label='RUT')
    NombreProf = django_filters.CharFilter(label='Nombre')
    class Meta:
        model = Profesor
        fields = ('RUTprof', 'NombreProf')