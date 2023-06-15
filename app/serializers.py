from rest_framework import serializers

from app.models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'