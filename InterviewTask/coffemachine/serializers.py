from rest_framework import serializers
from .models import CoffeMachine
from django.core.exceptions import ValidationError



class CoffeMachineSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CoffeMachine
        fields = ('__all__')

    


