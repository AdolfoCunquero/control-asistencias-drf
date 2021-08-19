from seccion.api.views import SeccionApiView, SeccionDetailApiView
from django.urls import path

urlpatterns = [
    path('section/', SeccionApiView.as_view()),
    path('section/<int:pk>/', SeccionDetailApiView.as_view()),    
]