from django.urls import path

from . import views

urlpatterns = [
#     path('', views.ListSequence.as_view()),
#     path('sequence', views.DetailSequence.as_view()),
    path('<str:sequence_id>', views.ListFileSequences),
#     path('sequence/<str:sequence_id>', views.ListFileSequences),
#     path('gb/<str:sequence_id>', views.genBankFile),
#     path('protein', views.DetailResult, name="sequence"),
]