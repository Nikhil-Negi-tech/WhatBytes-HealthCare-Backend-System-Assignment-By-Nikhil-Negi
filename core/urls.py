from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet, MappingViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)
router.register('mappings', MappingViewSet)

urlpatterns = router.urls