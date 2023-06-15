from rest_framework.routers import SimpleRouter
from .views import UploadViewset

urlpatterns = []

router = SimpleRouter()
router.register('accounts', UploadViewset)
urlpatterns = router.urls