from rest_framework import serializers
from .models import *

class LoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Load
        fields='__all__'
        
        