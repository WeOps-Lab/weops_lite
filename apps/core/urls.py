from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from apps.core.views.user_view import UserView

admin.site.site_title = "WeOps-Lite 管理"
admin.site.site_header = admin.site.site_title
public_router = routers.DefaultRouter()
public_router.register(r"api/public/user_view", UserView, basename="user_view")

urlpatterns = public_router.urls
