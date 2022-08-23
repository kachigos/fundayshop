from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users/', UserViewSet, basename='users')
router.register('post/', PostViewSet, basename='posts')
urlpatterns = router.urls


