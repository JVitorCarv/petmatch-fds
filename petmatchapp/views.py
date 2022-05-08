from django.views.generic import CreateView, DetailView, ListView

from petmatchapp.models import PetProfile

from .models import PetProfile


class HomePageView(ListView):
    model = PetProfile
    template_name = "home.html"


class PetDetailView(DetailView):
    model = PetProfile
    template_name = "pet_details.html"
    context_object_name = 'PetProfile'
    
class AddPetView(CreateView):
    model = PetProfile
    template_name = "add_pet.html"
    fields = '__all__'
