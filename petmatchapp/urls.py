from django.urls import path

from . import views

app_name = 'petmatchapp'

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
]

