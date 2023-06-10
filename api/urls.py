from django.urls import path, include
from .views import *

urlpatterns = [
    path('update/<int:pk>/', DetailToDo.as_view()),
    path('', ListToDo.as_view()),
    path('<int:pk>/', DetailOneToDo.as_view()),
    path('create', CreateToDo.as_view()),
    path('delete/<int:pk>/', DeleteToDo.as_view()),
    ]
