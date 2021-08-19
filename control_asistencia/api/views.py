from rest_framework.generics import CreateAPIView
from control_asistencia.api.serializers import ControlAsistenciaStoreSerializer
from rest_framework.permissions import IsAuthenticated

class ControlAsistenciaView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ControlAsistenciaStoreSerializer

    def perform_create(self, serializer):
        serializer.save(username_student=self.request.user)
        return super().perform_create(serializer)