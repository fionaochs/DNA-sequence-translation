from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListSequences.as_view()),
    path('<int:pk>/', views.DetailSequence.as_view()),
]