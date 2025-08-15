# Django ToDo App

Prosta, ale w pełni funkcjonalna aplikacja webowa typu "Lista Zadań" zbudowana w Pythonie przy użyciu frameworka Django. Projekt implementuje wszystkie podstawowe operacje CRUD (Create, Read, Update, Delete) i posiada system rejestracji oraz logowania użytkowników.

## Zrzut Ekranu

![Widok listy zadań]([screenshots/todo_list1.png, screenshots/todo_list2..png, screenshots3.png])
*Przykład: Aby dodać zrzut ekranu, zrób go, wrzuć do folderu w projekcie (np. `screenshots/main_view.png`) i podlinkuj tutaj.*

## Główne Funkcjonalności

*   **System Uwierzytelniania:** Użytkownicy mogą zakładać konta, logować się i wylogowywać.
*   **Prywatne Listy Zadań:** Każdy użytkownik ma dostęp tylko do swoich własnych zadań.
*   **Operacje CRUD:**
    *   **Tworzenie:** Dodawanie nowych zadań do listy.
    *   **Odczyt:** Wyświetlanie listy zadań.
    *   **Aktualizacja:** Edycja istniejących zadań i oznaczanie ich jako ukończone.
    *   **Usuwanie:** Kasowanie zadań z listy.
*   **Responsywny Design:** Interfejs użytkownika został zbudowany z użyciem frameworka Bootstrap i dostosowuje się do różnych rozmiarów ekranu.
*   **Zabezpieczenia:** Aplikacja uniemożliwia niezalogowanym użytkownikom dostęp do list zadań oraz blokuje próby edycji/usuwania cudzych zadań.

## Użyte Technologie

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, Bootstrap 5
*   **Baza Danych:** SQLite (dewelopersko)
*   **Środowisko:** Python Virtual Environment (venv)

## Instalacja i Uruchomienie Lokalne

Aby uruchomić projekt na swoim komputerze, postępuj zgodnie z poniższymi krokami:

1.  **Sklonuj repozytorium:**
    ```bash
    git clone https://github.com/Garseniuk/todo-project.git
    cd todo-project
    ```

2.  **Stwórz i aktywuj środowisko wirtualne:**
    ```bash
    # Dla macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # Dla Windows
    python -m venv venv
    .\venv\Scripts\activate
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

Aplikacja będzie dostępna w przeglądarce pod adresem `http://127.0.0.1:8000/`.