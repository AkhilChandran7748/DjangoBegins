
from rest_framework import routers
from myapps.views import BlogViewSet, UsersViewSet

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = router.urls


