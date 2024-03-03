from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/", include("app.urls", namespace='app')),
    path("myauth/", include("myauth.urls", namespace='myauth'))
]
