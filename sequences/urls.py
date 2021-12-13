from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListSequence.as_view()),
    path('sequence', views.DetailResult, name="sequence"),
    path('sequence/<str:protein>', views.DetailSequence.as_view()),
]