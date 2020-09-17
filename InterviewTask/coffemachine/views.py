from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .serializers import CoffeMachineSerializer
from .models import CoffeMachine
from django.shortcuts import get_object_or_404

# Create your views here.


class CoffeMachineViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = CoffeMachine.objects.all()
    serializer_class = CoffeMachineSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = CoffeMachine.objects.all()
        wlc=self.request.query_params.get('wlc', None)
        if wlc is not None:
            queryset = queryset.filter(water_line_compatible=wlc)
        type=self.request.query_params.get('type', None)
        if type is not None:
            queryset = queryset.filter(product_type=type)    
        return queryset
    