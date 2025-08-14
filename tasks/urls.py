# Wklej całą zawartość tego bloku kodu do tasks/urls.py

from django.urls import path
from .views import TaskList, RegisterPage, TaskCreate, TaskUpdate, TaskDelete
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    # URL do tworzenia zadania
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    # URL do edycji zadania. Zwróć uwagę na <int:pk> - to jest identyfikator (Primary Key) zadania.
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    # URL do usuwania zadania
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'), 
]