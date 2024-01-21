from django.urls import include, path
from rest_framework import routers

from apps.core.views.user_view import UserView

public_router = routers.DefaultRouter()
public_router.register(r'user_view', UserView, basename='user_view')

urlpatterns = [
    path("api/public/", include(public_router.urls)),
]
