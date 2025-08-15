
from django import forms
from django.forms import ModelForm
from .models import Task

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formularz do tworzenia i edycji zadań
class TaskForm(ModelForm):
    class Meta:
        model = Task
        # Wybieramy pola, które mają być w formularzu
        fields = ['title', 'description', 'completed']
        # Dodajemy widżety, aby nadać polom atrybuty HTML (np. klasy CSS)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz tytuł zadania'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dodaj opis...'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# Formularz do rejestracji, który dziedziczy po domyślnym formularzu Django
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',) # Dodajemy pole email
    
    # Dodajemy klasy Bootstrapa do pól formularza rejestracji
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})