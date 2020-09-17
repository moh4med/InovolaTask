from rest_framework import serializers
from .models import CoffePod
from django.core.exceptions import ValidationError



class CoffePodSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CoffePod
        fields = ('__all__')

    


