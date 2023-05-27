from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Pet(models.Model):
    
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField(max_length=20, default= 0)
    description = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    photo = models.ImageField(upload_to='images/', blank=True, null=True)


    def str(self):
        return f"{self.name}"
    
    

# class OnlineUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# class RegisterPet(models.Model):
#     online_user = models.OneToOneField(OnlineUser, on_delete=models.CASCADE)
#     name_pet = models.CharField(max_length=100)
#     breed = models.CharField(max_length=100)
#     age = models.FloatField(max_length=20)
#     description = models.TextField
#     phone = models.CharField(max_length=100)
#     email = models.EmailField()
#     city = models.CharField(max_length=100)
#     ##photo = models.ImageField(upload_to='pet', blank=True, null=True)

# Calendario

class Event(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    colorSelected = models.CharField(max_length=10)
    
    @property
    def get_html_url(self):
        url = reverse('recipes:event', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
# fim calendario

#medicine

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    med = models.CharField(max_length=50)
    time = models.DateTimeField(max_length=50)
    resp = models.CharField(max_length=50)
    def str(self):
        return f"{self.med}"
    
#fim medicine

# alergy

class Alergy(models.Model):
    title = models.CharField(max_length=50)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, default= 0) 
    def str(self):
        return f"{self.title}"

# fim alergy

# food

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.CharField(max_length=50)
    time = models.DateTimeField(max_length=50)
    resp = models.CharField(max_length=50)
    def str(self):
        return f"{self.food}"

# fim food