from django.test import TestCase
# Importujemy User, aby móc tworzyć testowych użytkowników
from django.contrib.auth.models import User
# Client to narzędzie do symulowania zapytań przeglądarki (GET, POST)
from django.test import Client
# reverse_lazy pozwala nam odwoływać się do URLi po ich nazwach
from django.urls import reverse_lazy

from .models import Task

class TaskModelAndViewsTests(TestCase):
    
    # Metoda setUp jest specjalną metodą, która uruchamia się PRZED każdym testem.
    # Używamy jej, aby przygotować "środowisko" dla naszych testów.
    def setUp(self):
        # Tworzymy dwóch testowych użytkowników. Baza danych jest czyszczona po każdym teście.
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')

        # Tworzymy zadanie i przypisujemy je do użytkownika nr 1
        self.task = Task.objects.create(
            title='Test Task for User 1',
            description='This is a test description.',
            user=self.user1
        )
        
        # Inicjalizujemy klienta (symulator przeglądarki)
        self.client = Client()

    # --- ZACZYNAMY TESTY ---
    # Nazwa każdej metody testowej MUSI zaczynać się od "test_".

    def test_login_required_for_task_list(self):
        """Test: Sprawdza, czy niezalogowany użytkownik jest przekierowany na stronę logowania."""
        
        # Symulujemy próbę wejścia na stronę główną ('tasks')
        response = self.client.get(reverse_lazy('tasks'))
        
        # Sprawdzamy, czy odpowiedź serwera to przekierowanie (kod 302)
        self.assertEqual(response.status_code, 302)
        
        # Sprawdzamy, czy serwer przekierowuje nas DOKŁADNIE na stronę logowania
        self.assertRedirects(response, '/login/?next=/')
        print("\nPASSED: test_login_required_for_task_list")
    
    def test_user_sees_only_their_tasks(self):
        """Test: Sprawdza, czy zalogowany użytkownik widzi tylko swoje zadania."""
        
        # Logujemy użytkownika nr 1
        self.client.login(username='user1', password='password123')
        
        # Wchodzimy na listę zadań jako użytkownik nr 1
        response = self.client.get(reverse_lazy('tasks'))
        
        # Sprawdzamy, czy w kontekście szablonu (na stronie) znajduje się zadanie użytkownika 1
        self.assertContains(response, 'Test Task for User 1')
        
        # Wylogowujemy użytkownika nr 1
        self.client.logout()
        
        # Logujemy użytkownika nr 2 (który nie ma żadnych zadań)
        self.client.login(username='user2', password='password123')
        
        # Wchodzimy na listę zadań jako użytkownik nr 2
        response = self.client.get(reverse_lazy('tasks'))

        # Sprawdzamy, czy na stronie NIE MA zadania, które należy do użytkownika 1
        self.assertNotContains(response, 'Test Task for User 1')
        print("PASSED: test_user_sees_only_their_tasks")


    def test_authenticated_user_can_create_task(self):
        """Test: Sprawdza, czy zalogowany użytkownik może utworzyć zadanie."""
        
        # Logujemy użytkownika nr 1
        self.client.login(username='user1', password='password123')
        
        # Liczba zadań przed dodaniem nowego
        task_count_before = Task.objects.count()
        
        # Symulujemy wysłanie formularza (metodą POST) na URL 'task-create'
        response = self.client.post(reverse_lazy('task-create'), {
            'title': 'New Task from Test',
            'description': 'This task was created by a test.',
            'completed': False
        })
        
        # Sprawdzamy, czy liczba zadań w bazie danych wzrosła o 1
        self.assertEqual(Task.objects.count(), task_count_before + 1)
        
        # Sprawdzamy, czy po utworzeniu zadania zostaliśmy przekierowani na stronę główną
        self.assertRedirects(response, reverse_lazy('tasks'))
        
        # Sprawdzamy, czy nowo utworzone zadanie jest przypisane do właściwego użytkownika
        new_task = Task.objects.get(title='New Task from Test')
        self.assertEqual(new_task.user, self.user1)
        print("PASSED: test_authenticated_user_can_create_task")