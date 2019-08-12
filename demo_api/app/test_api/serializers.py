from rest_framework import serializers

from app.test_api.models import *

class tabla_Serializer(serializers.ModelSerializer):
    class Meta:
        model = tabla
        fields = ('id', 'nombre', 'direccion', 'superficie', 'email')