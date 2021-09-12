from rest_framework import routers, urlpatterns
from .api import LeadViewset


router = routers.DefaultRouter()
router.register("api/leads", LeadViewset, "leads")

urlpatterns = router.urls
