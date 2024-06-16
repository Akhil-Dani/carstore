from rest_framework import serializers
from . models import Brand, Model, Buyer

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','brand']

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'model']

class BuyerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
       model = Buyer
       fields = ['id', 'user_id', 'phone', 'new_or_used']
    