from yourapp.views import GroupViewSet,ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'groups/(?P<territory>[^/.]+)', GroupViewSet)
router.register(r'profiles/(?P<territory>[^/.]+)', ProfileViewSet)
urlpatterns = router.urls
