from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class PetProfile(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    race = models.CharField(max_length=30)
    bio = models.TextField()
    pet_image = models.ImageField(upload_to='pet_image')
    
    def __str__(self):
        return self.name + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("petmatchapp:pet_detail", kwargs={"pk": self.pk})
    
    