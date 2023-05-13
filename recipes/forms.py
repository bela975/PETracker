from django.forms import ModelForm, DateInput,modelformset_factory
from .models import Event, Alergy, Medicine
from .models import Task
from django.forms.widgets import DateInput


class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ['task', 'due_date']
    widgets = {
      'due_date': DateInput(attrs={'type': 'date'})
    }


TaskFormSet = modelformset_factory(Task, form=TaskForm, extra=0)


class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class AlergyForm(ModelForm):
    class Meta:
        model = Alergy
        fields = '__all__'


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)
        self.fields['time'].input_formats = ('%Y-%m-%dT%H:%M',)