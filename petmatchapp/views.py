from django.views.generic import DetailView, ListView

from petmatchapp.models import PetProfile

from .models import PetProfile


class HomePageView(ListView):
    model = PetProfile
    template_name = "home.html"


class PetDetailView(DetailView):
    model = PetProfile
    template_name = 'pet_details.html'
