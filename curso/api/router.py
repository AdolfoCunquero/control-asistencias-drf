from rest_framework.routers import DefaultRouter
from curso.api.views import CursoApiViewSet

router_curso = DefaultRouter()
router_curso.register(prefix="course", basename='course', viewset=CursoApiViewSet)