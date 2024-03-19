"""
URL configuration for agendapersonal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from agenda_personal.views import ContactoListado, ContactoDetalle, ContactoCrear, ContactoActualizar, ContactoEliminar

urlpatterns = [
    path('admin/', admin.site.urls),

    # La ruta 'leer' en donde listamos todos los registros de la Base de Datos
    path('agenda_personal/', ContactoListado.as_view(template_name="contacto/index.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un registro
    path('agenda_personal/detalle/<int:pk>', ContactoDetalle.as_view(template_name="contacto/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo registro
    path('agenda_personal/crear', ContactoCrear.as_view(template_name="contacto/cear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un registro de la Base de Datos
    path('agenda_personal/editar/<int:pk>', ContactoActualizar.as_view(template_name="contacto/actualizar.html"),
         name='actualizar'),

    # La ruta 'eliminar' que usaremos para eliminar un registro de la Base de Datos
    path('agenda_personal/eliminar/<int:pk>', ContactoEliminar.as_view(), name='eliminar'),
]
