from django.urls import path, include
from rest_framework import routers

api_router = routers.DefaultRouter()

urlpatterns = [
    path(r"api/", include(api_router.urls)),
]
