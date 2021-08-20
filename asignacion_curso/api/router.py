from django.urls import path
from asignacion_curso.api.views import AsignacionCursoView, AsignacionCursoDetailView, AsignacionCursoStudentView

urlpatterns = [
    path('asignation/', AsignacionCursoView.as_view()),
    path('asignation/<int:pk>/', AsignacionCursoDetailView.as_view()),
    path('asignation/me/',AsignacionCursoStudentView.as_view()),
]