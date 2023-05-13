# recipes/models.py
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()
    # upload_to='pet'
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pet'


class Task(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='No description')
    completed = models.BooleanField(default=False)
    due_date = models.DateField()

    def __str__(self):
        return self.task


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    colorSelected = models.Charfield(max_lenght=1)

    @property
    def get_html_url(self):
        url = reverse('recipes:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
