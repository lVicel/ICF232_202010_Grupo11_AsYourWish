import django_filters
from .models import Profesor
Locales_Disponibles=[('Casa Matriz','Casa Matriz'),('Bellavista','Bellavista'),('Providencia','Providencia'),('La Florida','La Florida'),]


class Filtro_Profesor(django_filters.FilterSet):
    RUTprof = django_filters.CharFilter(label='RUT')
    NombreProf = django_filters.CharFilter(label='Nombre')
    ClaseProfesor = django_filters.CharFilter(label='Clase')
    LocalPerteneciente = django_filters.ChoiceFilter(label='Local', choices=Locales_Disponibles)
    class Meta:
        model = Profesor
        fields = ('RUTprof', 'NombreProf','LocalPerteneciente', 'ClaseProfesor') 