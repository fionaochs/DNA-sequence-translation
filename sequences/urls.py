from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListSequence.as_view()),
    path('sequence', views.DetailSequence.as_view()),
    path('sequence/<str:sequence_id>', views.ListFileSequences),
    path('protein/<str:sequence_id>', views.DetailResult, name="sequence"),
]