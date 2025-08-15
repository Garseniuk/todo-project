# Django ToDo App

Prosta, ale w pełni funkcjonalna aplikacja webowa typu "Lista Zadań" zbudowana w Pythonie przy użyciu frameworka Django. Projekt implementuje wszystkie podstawowe operacje CRUD, posiada system uwierzytelniania użytkowników i jest w pełni skonteneryzowany za pomocą Dockera.

## Zrzuty Ekranu

| Strona Logowania | Lista Zadań | Formularz Edycji |
| :---: | :---: | :---: |
| ![Widok strony logowania](screenshots/todo_list1.png) | ![Widok listy zadań](screenshots/todo_list2.png) | ![Widok formularza edycji](screenshots/todo_list3.png) |

## Główne Funkcjonalności

*   **System Uwierzytelniania:** Rejestracja, logowanie i wylogowywanie użytkowników.
*   **Prywatne Listy Zadań:** Każdy użytkownik ma dostęp tylko do swoich własnych zadań.
*   **Operacje CRUD:** Pełna obsługa tworzenia, odczytu, aktualizacji i usuwania zadań.
*   **Testy Jednostkowe:** Kluczowe funkcjonalności są pokryte testami automatycznymi.
*   **Konteneryzacja:** Aplikacja jest gotowa do uruchomienia w środowisku Docker.
*   **Responsywny Design:** Interfejs użytkownika zbudowany z użyciem Bootstrapa.

## Użyte Technologie

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, Bootstrap 5
*   **Baza Danych:** SQLite
*   **Testowanie:** Django `unittest`
*   **Konteneryzacja:** Docker, Docker Compose

## Uruchomienie Projektu

### Sposób 1: Uruchomienie z Dockerem (Zalecane)

Ta metoda jest najprostsza i gwarantuje, że aplikacja zadziała w każdym środowisku.

1.  **Wymagania:** Upewnij się, że masz zainstalowany i uruchomiony **Docker Desktop**.
2.  **Sklonuj repozytorium:**
    ```bash
    git clone https://github.com/Garseniuk/todo-project.git
    cd todo-project
    ```
3.  **Zbuduj i uruchom kontenery:**
    ```bash
    docker compose up --build
    ```
    *Pierwsze budowanie może zająć kilka minut.*

Aplikacja będzie dostępna w przeglądarce pod adresem `http://127.0.0.1:8000/`.

### Sposób 2: Uruchomienie lokalne z Pythonem

1.  **Sklonuj repozytorium i przejdź do folderu projektu.**
2.  **Stwórz i aktywuj środowisko wirtualne:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Zainstaluj zależności:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Wykonaj migracje bazy danych:**
    ```bash
    python manage.py migrate
    ```
5.  **Uruchom serwer deweloperski:**
    ```bash
    python manage.py runserver
    ```