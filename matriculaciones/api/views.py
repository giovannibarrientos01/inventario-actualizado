from rest_framework import viewsets, status
from rest_framework.response import Response
from matriculaciones.models import Matricula
from .serializers import MatriculacionesSerializer

class MatriculacionesViewset(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculacionesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 👇 Esto devuelve mensajes claros de error (qué campo falló y por qué)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
