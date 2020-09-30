from rest_framework import serializers
from .models import PAS_S40_Institution
class PAS_S40_InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAS_S40_Institution
        fields = "__all__"
