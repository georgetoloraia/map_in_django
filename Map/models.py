from django.db import models

# Create your models here.

class MapModel(models.Model):

    farti = models.ForeignKey('fartiModel', on_delete=models.CASCADE)
    fasi = models.ForeignKey('fasiModel', on_delete=models.CASCADE)
    statusi = models.ForeignKey('statusiModel', on_delete=models.CASCADE)
    mdebareoba = models.ForeignKey('mdebareobaModel', on_delete=models.CASCADE)


class FartiModel(models.Model):
    map_model = models.OneToOneField(MapModel, on_delete=models.CASCADE, primary_key=True)
    kvadratuli_farti = models.IntegerField()
    dan = models.IntegerField()
    mde = models.IntegerField()
    otaxebisRaodenoba = models.IntegerField()

class FasiModel(models.Model):
    map_model = models.OneToOneField(MapModel, on_delete=models.CASCADE, primary_key=True)
    dan = models.IntegerField()
    mde = models.IntegerField()

class StatusiModel(models.Model):
    map_model = models.OneToOneField(MapModel, on_delete=models.CASCADE, primary_key=True)
    chabarebuli = models.BooleanField(default=False)
    mshenebare = models.BooleanField(default=False)
    year = models.IntegerField()

class MdebareobaModel(models.Model):
    map_model = models.OneToOneField(MapModel, on_delete=models.CASCADE, primary_key=True)
    mdebareoba = models.TextField(max_length=50)
    lat = models.IntegerField()
    lng = models.IntegerField()