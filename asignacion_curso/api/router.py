from django.urls import path
from asignacion_curso.api.views import AsignacionCursoView, AsignacionCursoDetailView

urlpatterns = [
    path('asignation/', AsignacionCursoView.as_view()),
    path('asignation/<int:pk>/', AsignacionCursoDetailView.as_view()),
]