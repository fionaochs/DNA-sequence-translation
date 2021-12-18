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
    seq = Seq("CATGTAGACTAG")
    translated = seq.translate()
    transcribed = seq.reverse_complement().transcribe()

    data = [{'sequence':'CATGTAGACTAG', 'proteinName': 'YP_004678872', 'proteinLocation': '1370..1380', 'organism': 'NC_000852'},
            {'sequence':'CATGTAGACTAG', 'proteinName': translated, 'proteinLocation': '1353..2773', 'organism': 'NC_000852'},
            {'sequence':'CATGTAGACTAG', 'proteinName': transcribed, 'proteinLocation': '26262..26267', 'organism': 'NC_000852'},
            ]

# Found  "cgcaggcgct" in protein "YP_004678872.1" in NC_000852.5 in location 1371->1380

    print(data)
    return HttpResponse(data, content_type='application/json')
