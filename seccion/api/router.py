from seccion.api.views import SeccionApiView, SeccionDetailApiView, SeccionProfessorApiView
from django.urls import path

urlpatterns = [
    path('section/', SeccionApiView.as_view()),
    path('section/<int:pk>/', SeccionDetailApiView.as_view()),
    path('section/professor/', SeccionProfessorApiView.as_view()),    
]