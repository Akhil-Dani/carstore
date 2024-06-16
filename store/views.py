from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from .models import Brand, Model, Buyer
from .serializers import BrandSerializer, ModelSerializer, BuyerSerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['brand']
    search_fields = ['brand']
    
class ModelViewSet(ModelViewSet):
    # queryset = Model.objects.all()
    serializer_class = ModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['model']
    search_fields = ['model']

    def get_queryset(self):
        queryset = Model.objects.all()
        brand_id = self.request.query_params.get('brand_id')
        if brand_id is not None:
            queryset = queryset.filter(brand_id=brand_id)
        return queryset
    
class BuyerViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer



    