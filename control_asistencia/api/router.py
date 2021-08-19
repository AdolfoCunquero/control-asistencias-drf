from django.urls import path
from control_asistencia.api.views import ControlAsistenciaView

urlpatterns = [
    path('control_asistencia/', ControlAsistenciaView.as_view()),
]