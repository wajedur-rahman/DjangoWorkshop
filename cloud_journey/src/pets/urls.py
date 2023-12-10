

#cloud_journey/src/pets/urls.py
from django.urls import path
from pets.views import PetDetailView, PetsListView, PetCreateView, PetUpdateView

urlpatterns = [
    path("all/", PetsListView.as_view(), name="pet-list"),
    path("add/", PetCreateView.as_view(), name="add-pet"),
    path("update/<int:pk>/", PetUpdateView.as_view(), name="update-pet"),
    path("<int:pk>/", PetDetailView.as_view(), name="pet-detail"),
]