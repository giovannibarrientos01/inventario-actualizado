from rest_framework.routers import DefaultRouter
from matriculaciones.api.views import MatriculacionesViewset  
router = DefaultRouter()
router.register('matriculaciones', MatriculacionesViewset, basename='matriculaciones')
urlpatterns = router.urls   