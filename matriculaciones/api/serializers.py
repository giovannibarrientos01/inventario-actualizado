from rest_framework import serializers
from matriculaciones.models import Matricula


class MatriculacionesSerializer(serializers.ModelSerializer):
    class Meta: 
     model = Matricula 
     fields = '__all__'
