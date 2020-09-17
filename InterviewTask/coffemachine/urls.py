from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
router = DefaultRouter()
router.register(r'', views.CoffeMachineViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
