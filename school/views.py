from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import PAS_S40_Institution,PAS_S40_InstitutionSerializer
class PAS_40_CreateSchool(ModelViewSet):
    queryset = PAS_S40_Institution
    serializer_class = PAS_S40_InstitutionSerializer


class PAS_40_ViewSchool(ModelViewSet):
    queryset = PAS_S40_Institution.objects.all()
    serializer_class = PAS_S40_InstitutionSerializer
