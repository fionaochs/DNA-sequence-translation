from django.shortcuts import render
from rest_framework import generics
from .models import Sequence, Result
from .serializers import SequenceSerializer, ResultSerializer
from django.http import HttpResponse
from Bio.Seq import Seq

class ListSequence(generics.ListCreateAPIView):
    queryset = Sequence.objects.all()
    serializer_class = SequenceSerializer


class DetailSequence(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sequence.objects.all()
    serializer_class = SequenceSerializer

def DetailResult(request):
    seq = Seq('ACGT')
    translated = seq.reverse_complement().transcribe()

    data = [{'proteinName': 'protein 1', 'proteinLocation': 'protein 1 location'},{'proteinName': translated, 'proteinLocation': seq}]
    print(data)
    return HttpResponse(data, content_type='application/json')
