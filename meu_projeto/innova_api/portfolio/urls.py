from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet, ProjetoViewSet, TecnologiaViewSet

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'projetos', ProjetoViewSet)
router.register(r'tecnologias', TecnologiaViewSet)

urlpatterns = router.urls


router = DefaultRouter()