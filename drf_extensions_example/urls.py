from yourapp.views import GroupViewSet,ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'groups/(?P<territory>[^/.]+)/(?P<user_id>[^/.]+)', GroupViewSet)
router.register(r'profiles/(?P<territory>[^/.]+)/(?P<user_id>[^/.]+)', ProfileViewSet)
urlpatterns = router.urls
