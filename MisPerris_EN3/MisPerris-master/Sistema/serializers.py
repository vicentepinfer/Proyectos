from rest_framework import serializers
from .models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ["nombreMascota","razaMascota","descMascota","estadoMascota","fotoMascota"]