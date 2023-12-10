#cloud_journey/src/sneafur/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("admin/", admin.site.urls), path("pets/", include("pets.urls"))]