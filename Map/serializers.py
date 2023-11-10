from rest_framework import serializers
from .models import MapModel, FartiModel, FasiModel, StatusiModel, MdebareobaModel #coordinatModel

class MapModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapModel
        fields = '__all__'

class FartiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FartiModel
        fields = '__all__'

class FasiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FasiModel
        fields = '__all__'

class StatusiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusiModel
        fields = '__all__'

class MdebareobaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MdebareobaModel
        fields = '__all__'

# This serializer is test
# class coordinatModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = coordinatModel
#         fields = '__all__'