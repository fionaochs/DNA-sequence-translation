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

    data = [{'id': 1, 'sequence':'CATGTAGACTAG', 'proteinName': 'YP_004678872', 'proteinLocation': '1370..1380', 'organism': 'NC_000852'},
            {'id': 2, 'sequence':'CATGTAGACTAG', 'proteinName': 'YP_004678872', 'proteinLocation': '1353..2773', 'organism': 'NC_000852'},
            {'id': 3, 'sequence':'CATGTAGACTAG', 'proteinName': 'YP_004678872', 'proteinLocation': '26262..26267', 'organism': 'NC_000852'},
            ]

# Found  "cgcaggcgct" in protein "YP_004678872.1" in NC_000852.5 in location 1371->1380

    print(data)
    return JsonResponse(data, safe=False)

def ListFileSequences(request, sequence_id):
#  read all files in organisms folder
#     for filename in os.listdir('organisms'):
#         f = os.path.join('organisms', filename)
#         if os.path.isfile(f):
#                 record = SeqIO.read("../{f}", "fasta")
#     record = SeqIO.read("./NC_000852.5.fasta", "fasta")
#  'CGCAGGCGCT'
    print(sequence_id)
    files = ['NC_000852.fasta','NC_007346.fasta','NC_008724.fasta','NC_009899.fasta','NC_014637.fasta','NC_020104.fasta','NC_023423.fasta','NC_023640.fasta','NC_023719.fasta','NC_027867.fasta']

#     def checkFilesForSequence(request, sequence_id):
    for filename in files:
        file = 'NC_000852.fasta'
#         record = SeqIO.read("/Users/fiona.ochs/Documents/Projects/ginkgo2/NC_000852.fasta", "fasta")
        url = "/Users/fiona.ochs/Documents/Projects/ginkgo2/NC_000852.fasta"
#         url = "/Users/fiona.ochs/Documents/Projects/ginkgo2/{file}"
        record = SeqIO.read(url, "fasta")
        return calculateProtein(sequence_id, record)

def calculateProtein(sequence_id, record):
        upperCaseStrId = sequence_id.upper()
        seq = Seq(sequence_id)
        genome = record.seq

        foundSeqIdx = genome.find(sequence_id) # 1370
        if foundSeqIdx != -1:
            endIdx = foundSeqIdx + len(sequence_id)
            formattedLocation = str(foundSeqIdx) + '..' + str(endIdx) # 1370..1380
            organismName = record.name
            proteinName = seq.translate()
        else:
    #             formattedLocation = 'sequence not found'
            ListFileSequences(sequence_id)

        data = [{
        'id': 1,
        'sequence': str(sequence_id),
        'proteinName': str(proteinName),
        'proteinLocation': str(formattedLocation),
        'organism': str(organismName)
        }]
        print(data)
        return JsonResponse(data, safe=False)

# ID: NC_000852.5
# Name: NC_000852.5
# Description: NC_000852.5 Paramecium bursaria Chlorella virus 1, complete genome
# Number of features: 0
# Seq('GGGAGAACCAGGTGGGATTGACAGTGGTAAATGTGTTGACCACGAGTAAAAACA...TTT')
# filter Seq object for sequence