from django.urls import path
from . import views

urlpatterns = [
      path('<str:sequence_id>', views.CeleryFileSequencesGenbank),
      path('gb/<str:sequence_id>', views.ListFileSequencesGenbank),
]