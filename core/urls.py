from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet, MappingViewSet

router = DefaultRouter()
# for patients this will create endpoints like:
# - GET /api/patients/
# - POST /api/patients/
# - GET /api/patients/{id}/
# - PUT /api/patients/{id}/
# - DELETE /api/patients/{id}/
router.register('patients', PatientViewSet)
# for doctors this will create endpoints like:
# - GET /api/doctors/
# - POST /api/doctors/
# - GET /api/doctors/{id}/
# - PUT /api/doctors/{id}/
# - DELETE /api/doctors/{id}/
router.register('doctors', DoctorViewSet)
# for mappings this will create endpoints like:
# - GET /api/mappings/
# - POST /api/mappings/
# - GET /api/mappings/{id}/
# - PUT /api/mappings/{id}/
# - DELETE /api/mappings/{id}/
router.register('mappings', MappingViewSet)

urlpatterns = router.urls