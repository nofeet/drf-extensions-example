from rest_framework.routers import DefaultRouter
from yourapp.views import GroupViewSet,ProfileViewSet

router = DefaultRouter
router.register(r'groups', GroupViewSet)
router.register(r'profiles', ProfileViewSet)
urlpatterns = router.urls
