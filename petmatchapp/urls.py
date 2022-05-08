from django.urls import path

from . import views

app_name = 'petmatchapp'

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("pet/<int:pk>", views.PetDetailView.as_view(), name="pet_detail"),
    path("add/", views.AddPetView.as_view(), name="add_pet"),
    path("pet/edit/<int:pk>", views.UpdateView.as_view(), name="update_pet"),
    path("pet/delete/<int:pk>", views.DeletePetView.as_view(), name="delete_pet"),
]

