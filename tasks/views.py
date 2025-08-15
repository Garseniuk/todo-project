from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView # Potrzebne do widoku rejestracji
from django.urls import reverse_lazy
from .forms import TaskForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm # Wbudowany formularz Django do tworzenia użytkowników
from django.contrib.auth import login # Funkcja do logowania użytkownika po rejestracji

from .models import Task
# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks' # Zmienia domyślną nazwę 'object_list' na 'tasks' w szablonie

    # Ta metoda jest kluczowa!
    # Nadpisujemy ją, aby każdy użytkownik widział tylko swoje zadania.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrujemy zadania, aby należały do zalogowanego użytkownika
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        # Dodajemy licznik nieukończonych zadań
        context['count'] = context['tasks'].filter(completed=False).count()
        return context

class RegisterPage(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    # Używamy reverse_lazy, ponieważ URL jest przetwarzany, zanim konfiguracja URL projektu zostanie załadowana.
    success_url = reverse_lazy('tasks') 

    # Ta metoda jest wywoływana, gdy formularz zostanie poprawnie wypełniony i wysłany.
    def form_valid(self, form):
        # Zapisujemy nowego użytkownika w bazie danych.
        user = form.save()
        # Jeśli użytkownik został poprawnie stworzony, logujemy go.
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
        
    # Ta metoda zapobiega sytuacji, w której zalogowany użytkownik
    # mógłby wejść na stronę rejestracji.
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(*args, **kwargs)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # Określamy, które pola z modelu mają być widoczne w formularzu.
    # Nie chcemy, aby użytkownik mógł ręcznie przypisać zadanie do kogoś innego.
    form_class = TaskForm
    # Po pomyślnym utworzeniu zadania, przekieruj użytkownika z powrotem na listę zadań.
    success_url = reverse_lazy('tasks')

    # Ta metoda jest wywoływana, gdy formularz jest poprawny.
    # Nadpisujemy ją, aby automatycznie przypisać zadanie do zalogowanego użytkownika.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    # Używamy tych samych pól, co przy tworzeniu.
    form_class = TaskForm
    success_url = reverse_lazy('tasks')

    def get_queryset(self):
        # Użytkownik może edytować tylko swoje własne zadania
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task' # Zmieniamy nazwę obiektu w szablonie
    success_url = reverse_lazy('tasks')

    def get_queryset(self):
        # Użytkownik może usuwać tylko swoje własne zadania
        owner = self.request.user
        return self.model.objects.filter(user=owner)