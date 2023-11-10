from rest_framework import viewsets
from .models import MapModel, FartiModel, FasiModel, StatusiModel, MdebareobaModel
from .serializers import MapModelSerializer, FartiModelSerializer, FasiModelSerializer, StatusiModelSerializer, MdebareobaModelSerializer
from .filters import MapModelFilter, FartiModelFilter, FasiModelFilter, StatusiModelFilter, MdebareobaModelFilter

class MapModelViewSet(viewsets.ModelViewSet):
    queryset = MapModel.objects.all()
    serializer_class = MapModelSerializer
    filterset_class = MapModelFilter

class FartiModelViewSet(viewsets.ModelViewSet):
    queryset = FartiModel.objects.all()
    serializer_class = FartiModelSerializer
    filterset_class = FartiModelFilter

class FasiModelViewSet(viewsets.ModelViewSet):
    queryset = FasiModel.objects.all()
    serializer_class = FasiModelSerializer
    filterset_class = FasiModelFilter

class StatusiModelViewSet(viewsets.ModelViewSet):
    queryset = StatusiModel.objects.all()
    serializer_class = StatusiModelSerializer
    filterset_class = StatusiModelFilter

class MdebareobaModelViewSet(viewsets.ModelViewSet):
    queryset = MdebareobaModel.objects.all()
    serializer_class = MdebareobaModelSerializer
    filterset_class = MdebareobaModelFilter
