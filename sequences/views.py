from django.shortcuts import render
from rest_framework import generics
from .models import Sequence, Result
from .serializers import SequenceSerializer, ResultSerializer
from django.http import HttpResponse, JsonResponse
from Bio.Seq import Seq
from Bio import SeqIO
import os

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
            {'sequence':'CATGTAGACTAG', 'proteinName': 'YP_004678872', 'proteinLocation': '1353..2773', 'organism': 'NC_000852'},
            {'sequence':'CATGTAGACTAG', 'proteinName': 'YP_004678872', 'proteinLocation': '26262..26267', 'organism': 'NC_000852'},
            ]

# Found  "cgcaggcgct" in protein "YP_004678872.1" in NC_000852.5 in location 1371->1380

    print(data)
    return JsonResponse(data, safe=False)

def readFastaFiles(request):
#  read all files in organisms folder
    for filename in os.listdir('organisms'):
        f = os.path.join('organisms', filename)
        if os.path.isfile(f):
                record = SeqIO.read("../{f}", "fasta")

    record = SeqIO.read("../organisms/NC_000852.5.fasta", "fasta")
    genome = record.seq
#     convert request.sequence str to uppercase? str.upper()

    foundSeqIdx = genome.find(request.sequence) # 1370
    endIdx = foundSeqIdx + len(request.sequence)
    formattedLocation = str(foundSeqIdx) + '..' + str(endIdx) # 1370..1380
    organismName = record.name
    proteinName = request.sequence.translate()

# ID: NC_000852.5
# Name: NC_000852.5
# Description: NC_000852.5 Paramecium bursaria Chlorella virus 1, complete genome
# Number of features: 0
# Seq('GGGAGAACCAGGTGGGATTGACAGTGGTAAATGTGTTGACCACGAGTAAAAACA...TTT')
# filter Seq object for sequence

# find index of start of substr (sequence)
# that length + length of sequnce gives start and end of location
#