from django.forms import ModelForm
from django.forms.widgets import DateInput
from recipes.models import Event, Pet
from .models import Medicine, Alergy, Food


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'breed', 'description', 'phone', 'email', 'photo' )
        exclude = ['user']

class EventForm(ModelForm):
  class Meta:
    model = Event
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['med','resp','time']
        widgets = {
            'time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)
        self.fields['time'].input_formats = ('%Y-%m-%dT%H:%M',)

class AlergyForm(ModelForm):
    class Meta:
        model = Alergy
        fields =  ['title']

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['food','resp','time']
        widgets = {
            'time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.fields['time'].input_formats = ('%Y-%m-%dT%H:%M',)