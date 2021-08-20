from django.urls import path
from estadisticas.api.views import EstadisticaPorCursoView, EstadisticaPorCicloView, EstadisticaPorEstudianteView

urlpatterns = [
    path('statistics/por_curso/',EstadisticaPorCursoView.as_view()),
    path('statistics/por_ciclo/',EstadisticaPorCicloView.as_view()),
    path('statistics/por_estudiante/',EstadisticaPorEstudianteView.as_view()),
]