from xml.dom.minidom import Document
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

app_name = 'petmatchapp'

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("pet/<int:pk>", views.PetDetailView.as_view(), name="pet_detail"),
    path("add/", views.AddPetView.as_view(), name="add_pet"),
    path("settings", views.SettingsView.as_view(), name="settings"),
    path("profile", views.profileView.as_view(), name="profile"),

    #path("pet/edit/<int:pk>", views.UpdateView.as_view(), name="update_pet"),
    #path("pet/delete/<int:pk>", views.DeletePetView.as_view(), name="delete_pet"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


