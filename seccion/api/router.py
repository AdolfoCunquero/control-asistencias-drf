from seccion.api.views import SeccionApiView, SeccionDetailApiView#SeccionUpdateView, SeccionCreateView, SeccionListView
from django.urls import path

urlpatterns = [
    path('section/', SeccionApiView.as_view()),
    path('section/<int:pk>/', SeccionDetailApiView.as_view()),
    # path('section/create/', SeccionCreateView.as_view()),
    # path('section/<int:pk>/', SeccionUpdateView.as_view()),
    
]