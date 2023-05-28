from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from recipes.models import Pet, Medicine, Food
from .forms import AlergyForm, BackgroundColorForm, MedicineForm, PetForm, FoodForm, Taskanban, TaskanbanForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime, date
from django.views import generic
from .models import *
from .utils import Calendar
from .forms import EventForm


# login

def login_user(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('recipes:home')
        else:
            messages.success(request, ("Something is wrong! Password or name is incorrect."))
            return redirect('recipes:login')   

    else:
        return render(request, 'login.html')
    
@login_required(login_url='recipes:login')
def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('recipes:login')

# fim login

# registrando login

def register_user(request):
    if request.method == "GET":
        return render(request, 'register_user.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("A user with this name already exists.")
        user = User.objects.create_user(username=username, email=email, 
                                        password=senha)
        user.save()

        return redirect('recipes:login')
    
# fim registrando login
 
@login_required(login_url='recipes:login')
def home_choose_pet(request):
    return render(request, "home.html", {"pets": Pet.objects.all()})

@login_required(login_url='recipes:login')
def register_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:home')
    else:
        form = PetForm()
    return render(request, 'register_pet.html', {"form":form, "pets": Pet.objects.all()})



@login_required(login_url='recipes:login')
def pet_home(request):
    if request.method == "POST":
        alergy_form = AlergyForm(request.POST)
        background_color_form = BackgroundColorForm(request.POST)
        if alergy_form.is_valid():
            alergy_form.save()
            return redirect("/home_pet")
        
        if background_color_form.is_valid():
            pet = Pet.objects.first()
            pet.background_color = background_color_form.cleaned_data['background_color']
            pet.save()
            return redirect("/home_pet")
    else:
        alergy_form = AlergyForm()
        background_color_form = BackgroundColorForm()

    pet = Pet.objects.first()
    background_color = pet.background_color if pet else '#FFFFFF'

    return render(request, 'home_pet.html', 
                   {"alergy_form": alergy_form,
                    "alergies": Alergy.objects.all(),
                   "background_color_form": background_color_form,
                   "background_color": background_color,
                   "pets": Pet.objects.all(),
                    })



def alergy_detail(request, id):
    alergy = get_object_or_404(Alergy, pk=id)
    return render(request, "alergy_detail.html", {"alergy": alergy})


def delete_alergy(request, id):
    alergy = get_object_or_404(Alergy, pk=id)
    alergy.delete()
    return redirect("/home_pet")
  
 

# calendario

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('day', None))

        recipes = Calendar(d.year, d.month)
        
        
        html_recipes = recipes.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_recipes)
        return context
    
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

def delete_event(event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('recipes:calendar')

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

# fim calendario

# medicine

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

def delete_medicine(request, id):
    medicine = get_object_or_404(Medicine, pk=id)
    medicine.delete()
    return redirect("/medicine")

def medicine_detail(request, id):
    medicine = get_object_or_404(Medicine, pk=id)
    return render(request, "medicine_detail.html", {"medicine": medicine})

# fim medicine


# food 

def food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()
            return redirect("/food")
    else:
        form = FoodForm()
        foods = Food.objects.filter(user=request.user) if request.user.is_authenticated else []
        return render(request, 'food.html', {"form": form, "foods": foods})


def food_detail(request, id):
    food = get_object_or_404(Food, pk=id)
    return render(request, "food_detail.html", {"food": food})

def delete_food(request, id):
    food = get_object_or_404(Food, pk=id)
    food.delete()
    return redirect("/food")

# fim food

#kanban - checklist

def kanban(request, show_history='False'):
    show_history = show_history == 'True'
    tasks = Taskanban.objects.filter(status__in=['to_do', 'in_progress', 'done', 'history'])
    return render(request, 'kanban.html', {'tasks': tasks, 'show_history': show_history})


def add_task(request):
    if request.method == 'POST':
        task_name = request.POST['task']
        responsible = request.POST['responsible']
        due_date = request.POST['due-date']
        task = Taskanban(name=task_name, responsible=responsible, due_date=due_date)
        task.save()
    return redirect('recipes:kanban')

def remove_task(request, task_id):
    task = Taskanban.objects.get(id=task_id)
    task.delete()
    return redirect('/kanban')


def move_task(request, task_id):
    print(request)
    print("View move_task called with task_id:", task_id)
    task = Taskanban.objects.get(id=task_id)
    print("Task before update:", task)
    if task.status == 'to_do':
        task.status = 'in_progress'
    elif task.status == 'in_progress':
        task.status = 'done'
    elif task.status == 'done':
        task.status = 'history'
    task.save()
    print("Task after update:", task)
    return redirect('/kanban')

def move_task_back(request, task_id):
    task = Taskanban.objects.get(id=task_id)
    if task.status == 'in_progress':
        task.status = 'to_do'
    elif task.status == 'done':
        task.status = 'in_progress'
    elif task.status == 'history':
        task.status = 'done'
    task.save()
    return redirect('/kanban')

def restore_task(request, task_id):
    task = Taskanban.objects.get(id=task_id)
    task.status = 'to_do'
    task.save()
    return redirect('/kanban')

#kanban - checklist

