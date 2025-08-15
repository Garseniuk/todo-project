from django.db import models
from django.contrib.auth.models import User # Importujemy wbudowany model użytkownika Django

# Create your models here.

class Task(models.Model):
    # To jest najważniejsza część: łączymy zadanie z użytkownikiem.
    # ForeignKey to relacja "jeden do wielu" (jeden użytkownik może mieć wiele zadań).
    # on_delete=models.CASCADE oznacza, że jeśli użytkownik zostanie usunięty, jego zadania również.
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    
    # Proste pole tekstowe na tytuł zadania, maksymalnie 200 znaków.
    title = models.CharField(max_length=200)
    
    # Dłuższe pole tekstowe na opis. `blank=True` oznacza, że pole jest opcjonalne.
    description = models.TextField(blank=True)
    
    # Pole typu prawda/fałsz. `default=False` ustawia domyślną wartość na "nieukończone".
    completed = models.BooleanField(default=False)
    
    # Pole z datą i czasem. `auto_now_add=True` automatycznie ustawi datę utworzenia zadania.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Ta metoda mówi Django, jak wyświetlać obiekt w panelu admina. Zobaczymy jego tytuł.
        return self.title

    class Meta:
        # Ta opcja sprawia, że zadania na liście będą domyślnie sortowane
        # według statusu ukończenia (nieukończone na górze).
        ordering = ['completed']