import django_filters
from .models import MapModel, FartiModel, FasiModel, StatusiModel, MdebareobaModel #coordinatModel

class MapModelFilter(django_filters.FilterSet):
    class Meta:
        model = MapModel
        fields = '__all__'

class FartiModelFilter(django_filters.FilterSet):
    class Meta:
        model = FartiModel
        fields = '__all__'

class FasiModelFilter(django_filters.FilterSet):
    class Meta:
        model = FasiModel
        fields = '__all__'

class StatusiModelFilter(django_filters.FilterSet):
    class Meta:
        model = StatusiModel
        fields = '__all__'

class MdebareobaModelFilter(django_filters.FilterSet):
    class Meta:
        model = MdebareobaModel
        fields = '__all__'
