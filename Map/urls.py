from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MapModelViewSet, FartiModelViewSet, FasiModelViewSet, StatusiModelViewSet, MdebareobaModelViewSet

router = DefaultRouter()
router.register(r'mapmodels', MapModelViewSet)
router.register(r'fartimodels', FartiModelViewSet)
router.register(r'fasimodels', FasiModelViewSet)
router.register(r'statusimodels', StatusiModelViewSet)
router.register(r'mdebareobamodels', MdebareobaModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
