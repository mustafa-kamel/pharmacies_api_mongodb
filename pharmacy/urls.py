from rest_framework import routers

from pharmacy.views import PharmacyViewSet

router = routers.DefaultRouter()
router.register(r"pharmacies", PharmacyViewSet, basename="pharmacy")

urlpatterns = router.urls
