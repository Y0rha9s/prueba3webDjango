"""
URL configuration for carniceria_carvajal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from carniceria_carvajal.views import view_index
from carniceria_carvajal.views import view_vacuno
from carniceria_carvajal.views import view_ave
from carniceria_carvajal.views import view_cerdo
from carniceria_carvajal.views import view_formulario
from carniceria_carvajal.views import view_contactanos
from carniceria_carvajal.views import view_region
from carniceria_carvajal.views import view_registro
from carniceria_carvajal.views import view_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', view_index.index),
    path('', view_index.index),
    path('vacuno/', view_vacuno.vacuno),
    path('ave/', view_ave.ave),
    path('cerdo/', view_cerdo.cerdo),
    path('formulario/', view_formulario.formulario),
    path('formulario/save', view_formulario.save),
    path('contactanos/', view_contactanos.contactanos),
    path('region', view_region.region),
    path('registro', view_registro.registro),
    path('registro/save', view_registro.save),
    path('login', view_login.login),
]
