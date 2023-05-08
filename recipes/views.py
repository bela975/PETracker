from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib import messages
from .models import Pet, Task
from .forms import TaskForm, TaskFormSet
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm


def home(request):
    lista_pet = Pet.objects.all()
    return render(request, 'home.html', {

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


def perfis_pet(request):
    pet = Pet.objects.filter(active=True)
    return render(request, 'pet.html', {'pet': pet})


@login_required(login_url='/login/')
def todo_list(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    tasks = Task.objects.filter(pet=pet)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.pet = pet
            task.save()
            return redirect('todo_list', pet_id=pet_id)
    else:
        form = TaskForm()

    if request.POST.get('completed_task_id'):
        completed_task = Task.objects.get(id=request.POST['completed_task_id'])
        completed_task.delete()

    context = {
        'pet': pet,
        'tasks': tasks,
        'form': form
    }

    return render(request, 'todo_list.html', context)


@login_required(login_url='/login/')
def register_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        description = request.POST.get('description')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')
        user = request.user
        pet = Pet.objects.create(name=name, breed=breed, description=description, phone=phone, email=email, photo=photo,
                                 user=user)
        return redirect('recipes:pet')
    else:
        return render(request, 'register_pet.html')


@login_required(login_url='/login/')
def set_pet(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    user = request.user
    pet = Pet.objects.create(name=name, email=email, phone=phone, description=description, photo=file, user=user)

    return redirect('recipes:pet')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        recipes = Calendar(d.year, d.month)

        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        # Call the formatmonth method, which returns our calendar as a table
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
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('recipes:calendar'))
    return render(request, 'event.html', {'form': form})


def kanban(request):
    return render(request, 'kanban.html')


def Lista_pet(request):
    lista_pet = Pet.objects.all()
    return render(request, 'home.html', {
        'lista_pet': lista_pet,
    })


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        recipes = Calendar(d.year, d.month)

        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = recipes.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
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
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('recipes:calendar'))
    return render(request, 'event.html', {'form': form})