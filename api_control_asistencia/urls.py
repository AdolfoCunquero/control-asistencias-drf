"""api_control_asistencia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from drf_yasg import openapi
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from curso.api.router import router_curso

schema_view = get_schema_view(
    openapi.Info(
        title="Control Asistencias",
        default_version='v1',
        description='Documentacion de API Control asistencias',
        terms_of_service='',
        contact = openapi.Contact(email='adolfo@gmail.com'),
        license = openapi.License(name='BSD License'),
    ),
    public=True,
    #permission_classes=
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('user.api.router')),
    path('api/', include(router_curso.urls)),
    path('api/', include('seccion.api.router')),
    path('api/', include('asignacion_curso.api.router')),
    path('api/', include('control_asistencia.api.router')),
    path('api/', include('estadisticas.api.router')),
]
