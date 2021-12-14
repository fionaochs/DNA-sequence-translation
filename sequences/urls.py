from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListSequence.as_view()),
    path('sequence', views.ListSequence.as_view()),
#     path('sequence/<str:protein>', views.DetailSequence.as_view()),
    path('protein', views.DetailResult, name="sequence"),
]