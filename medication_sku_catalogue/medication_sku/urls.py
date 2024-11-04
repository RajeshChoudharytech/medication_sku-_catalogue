from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicationSKUViewSet

router = DefaultRouter()
router.register(r'Medicationsku', MedicationSKUViewSet, basename='Medicationsku')

urlpatterns = [
    path('', include(router.urls)), 
]