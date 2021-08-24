from django.urls import path
from control_asistencia.api.views import ControlAsistenciaView,ControlAsistenciaListView

urlpatterns = [
    path('control_asistencia/', ControlAsistenciaView.as_view()),
    path('control_asistencia/list/', ControlAsistenciaListView.as_view()),
]