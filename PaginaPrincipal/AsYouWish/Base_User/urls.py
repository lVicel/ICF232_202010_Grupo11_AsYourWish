from django.conf.urls import url
from AsYouWish.Base_User.views import CrearUsuario

urlpatterns = [
    url('CrearUsuarios/', CrearUsuario.as_view(), name="CrearUsuario")
]