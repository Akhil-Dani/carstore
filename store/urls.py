from django.urls import path, include
from rest_framework_nested import routers
from . import views



router = routers.DefaultRouter()
router.register('brand', views.BrandViewSet)
router.register('buyer', views.BuyerViewSet)


brand_router = routers.NestedDefaultRouter(router, 'brand', lookup='brand')
brand_router.register('model', views.ModelViewSet, basename='brand-model')


urlpatterns = router.urls + brand_router.urls