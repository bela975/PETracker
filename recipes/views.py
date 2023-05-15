from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib import messages
from .models import Pet, Task, Alergy, Medicine
from .forms import TaskForm, TaskFormSet, AlergyForm, MedicineForm
from datetime import datetime, timedelta, date
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm


@login_required(login_url='login')
def home(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id, user=request.user)
    
    if request.method == "POST":
        form = AlergyForm(request.POST)
        if form.is_valid():
            alergy = form.save(commit=False)
            alergy.pet = pet
            alergy.save()
            return redirect("/home/{}".format(pet_id))
    else:
        form = AlergyForm()

    lista_pet = Pet.objects.filter(user=request.user)

    return render(request, 'home.html',
                  {"form": form,
                   "alergies": Alergy.objects.filter(pet=pet),
                   "lista_pet": lista_pet,
                   })


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('já existe um usuário com esse nome!')
        
        user = User.objects.create_user(username=username, email=email, 
                                        password=senha)
        user.save()

        return redirect('recipes:login')
    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return redirect('recipes:pet')
        else:
            messages.error(request, 'Usuário e senha inválido, Favor tentar novamente.')
        return redirect('recipes:login')


@login_required(login_url="/auth/login/")
def plataforma(request):
    return render(request, 'pet.html')


@login_required(login_url='login')
def pet(request):
    if request.user.is_authenticated:
        pet = Pet.objects.filter(active=True, user=request.user)
    else:
        pet = []
    return render(request, 'pet.html', {'pet': pet})

@login_required(login_url='/login/')
def register_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        description = request.POST.get('description')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        ##photo = request.FILES.get('photo')
        user = request.user
        pet = Pet.objects.create(name=name, breed=breed, email=email, phone=phone, description=description, user=request.user)
        return redirect('recipes:pet')
    else:
        return render(request, 'register_pet.html')


@login_required(login_url='/login/')
def set_pet(request):
    name = request.POST.get('name')
    breed = request.POST.get('breed')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    user = request.user
    pet = Pet.objects.create(name=name, breed=breed, description=description, phone=phone, email=email, user=request.user)
    
    return redirect('recipes:pet')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('day', None))

        recipes = Calendar(d.year, d.month)
        
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        
        html_recipes = recipes.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_recipes)
        return context
    
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def event(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('recipes:calendar'))

    event_color_value = event_color(instance)
    context = {'form': form, 'event_color': event_color_value}
    return render(request, 'event.html', context)


# def event_delete(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     event.delete()
#     return redirect(request, "/calendar")

def kanban(request):
    return render(request, 'kanban.html')

def Lista_pet(request):
    lista_pet = Pet.objects.all()
    return render(request, 'home.html',{
        'lista_pet':lista_pet,
    })

def medicine(request):
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            return redirect("/medicine")
    else:
        form = MedicineForm()
        medicines = Medicine.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'medicine.html', {"form": form, "medicines": medicines})

def alergy_detail(request, id):
    alergy = get_object_or_404(Alergy, pk=id)
    return render(request, "alergy_detail.html", {"alergy": alergy})

def delete_alergy(request, id):
    alergy = get_object_or_404(Alergy, pk=id)
    alergy.delete()
    return redirect("/home")

def medicine_detail(request, id):
    medicine = get_object_or_404(Medicine, pk=id)
    return render(request, "medicine_detail.html", {"medicine": medicine})

def delete_medicine(request, id):
    medicine = get_object_or_404(Medicine, pk=id)
    medicine.delete()
    return redirect("/medicine")

def event_color(instance):
    color = '#978DCC'
    color_selected = instance.colorSelected
    if color_selected == 'purple':
        color = '#978DCC' #roxo gato (default)
    elif color_selected == 'orange':
        color = '#FAA42B' #lalanja dog
    elif color_selected == 'blue':
        color = '#00B7D9' #azul fofo papagaio
    elif color_selected == 'green':
        color = '#4FD881' #verde mama & bela
    else:
        color = color
    return color

