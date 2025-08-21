# Django ToDo App

[![Django CI](https://github.com/Garseniuk/todo-project/actions/workflows/django-ci.yml/badge.svg)](https://github.com/Garseniuk/todo-project/actions/workflows/django-ci.yml)

Prosta, ale w pełni funkcjonalna aplikacja webowa typu "Lista Zadań" zbudowana w Pythonie przy użyciu frameworka Django. Projekt implementuje wszystkie podstawowe operacje CRUD, posiada system uwierzytelniania użytkowników, jest w pełni skonteneryzowany za pomocą Dockera i automatycznie testowany przy użyciu GitHub Actions.

## Zrzuty Ekranu

| Strona Logowania | Lista Zadań | Formularz Edycji |
| :---: | :---: | :---: |
| ![Widok strony logowania](screenshots/todo_list1.png) | ![Widok listy zadań](screenshots/todo_list2.png) | ![Widok formularza edycji](screenshots/todo_list3.png) |

## Główne Funkcjonalności

*   **System Uwierzytelniania:** Rejestracja, logowanie i wylogowywanie użytkowników.
*   **Prywatne Listy Zadań:** Każdy użytkownik ma dostęp tylko do swoich własnych zadań.
*   **Operacje CRUD:** Pełna obsługa tworzenia, odczytu, aktualizacji i usuwania zadań.
*   **Automatyczne Testy:** Kluczowe funkcjonalności są pokryte testami jednostkowymi.
*   **Konteneryzacja:** Aplikacja jest gotowa do uruchomienia w środowisku Docker.
*   **CI/CD Pipeline:** Automatyczny proces na GitHub Actions uruchamia testy po każdym commicie do gałęzi `main`.
*   **Responsywny Design:** Interfejs użytkownika zbudowany z użyciem Bootstrapa.

## Użyte Technologie

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, Bootstrap 5
*   **Baza Danych:** SQLite
*   **Testowanie:** `unittest` (wbudowany w Django)
*   **DevOps:** Docker, Docker Compose, Git, GitHub Actions (CI/CD)

## Uruchomienie Projektu

### Sposób 1: Uruchomienie z Dockerem (Zalecane)

1.  **Wymagania:** Upewnij się, że masz zainstalowany i uruchomiony **Docker Desktop**.
2.  **Sklonuj repozytorium i przejdź do folderu projektu.**
3.  **Zbuduj i uruchom kontenery:**
    ```bash
    docker compose up --build
    ```
Aplikacja będzie dostępna w przeglądarce pod adresem `http://127.0.0.1:8000/`.

### Sposób 2: Uruchomienie lokalne z Pythonem

1.  **Sklonuj repozytorium i przejdź do folderu projektu.**
2.  **Stwórz i aktywuj środowisko wirtualne.**
3.  **Zainstaluj zależności (`pip install -r requirements.txt`).**
4.  **Wykonaj migracje (`python manage.py migrate`).**
5.  **Uruchom serwer (`python manage.py runserver`).**