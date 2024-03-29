from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('^user', views.UserViewSet)

urlpatterns = router.urls
