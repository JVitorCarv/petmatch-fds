from django.urls import path

from . import views

app_name = 'petmatchapp'

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("pet_details/<int:pk>/", views.PetDetailView.as_view(), name="pet-details")
]

