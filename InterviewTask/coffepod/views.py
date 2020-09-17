from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .serializers import CoffePodSerializer
from .models import CoffePod
from django.shortcuts import get_object_or_404

# Create your views here.


class CoffePodViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = CoffePod.objects.all()
    serializer_class = CoffePodSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = CoffePod.objects.all()
        size=self.request.query_params.get('size', None)
        if size is not None:
            queryset = queryset.filter(size_type=size)
        type=self.request.query_params.get('type', None)
        if type is not None:
            queryset = queryset.filter(product_type=type)
        flavor=self.request.query_params.get('flavor', None)
        if flavor is not None:
            queryset = queryset.filter(flavor_type=flavor)        
        return queryset
    