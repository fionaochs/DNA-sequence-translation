from django.urls import path
from . import views

urlpatterns = [
    path('<str:sequence_id>', views.ListFileSequences),
    path('gb/<str:sequence_id>', views.genBankFile),
    path('gb2/<str:sequence_id>', views.ListFileSequencesGenbank)
]