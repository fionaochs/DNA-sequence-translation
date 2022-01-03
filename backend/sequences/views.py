from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from Bio.Seq import Seq
from Bio import SeqIO
from tasks import findProtein
from celery.result import AsyncResult
from django_celery_results.models import TaskResult
from django.core import serializers

def CeleryFileSequencesGenbank(request, sequence_id):
  strSeq = str(sequence_id)
  task = findProtein.delay(strSeq)

  return JsonResponse({'taskId':task.id}, safe=False)

def get_context_data(self, *args, **kwargs):
     allResults = TaskResult.objects.all()
     filtered = TaskResult.objects.filter().values()
     results = [x for x in allResults if x=='\'result\'']
     data = serializers.serialize('json', TaskResult.objects.all())
     return JsonResponse(data, safe=False)




def ListFileSequencesGenbank(request, sequence_id):
  files = ['NC_000852.gb', 'NC_009899.gb', 'NC_008724.gb', 'NC_007346.gb','NC_014637.gb','NC_020104.gb','NC_023423.gb','NC_023640.gb','NC_023719.gb','NC_027867.gb']

  for filename in files:
        url = './organisms/{}'.format(filename)
        for rec in SeqIO.parse(url, "genbank"):
            for feature in rec.features:
                seq = Seq(sequence_id)
                upperSeq = seq.upper()
                genome = rec.seq
                foundSeqIdx = genome.find(upperSeq)

                if foundSeqIdx != -1:
                    startLocation = feature.location.start.position
                    endLocation = feature.location.end.position
                    sequenceLength = foundSeqIdx + len(sequence_id)

                    if feature.type == "CDS" and (startLocation < foundSeqIdx and endLocation > sequenceLength):
                        protein_id = feature.qualifiers["protein_id"][0]
                        endIdx = foundSeqIdx + len(sequence_id)
                        formattedLocation = str(foundSeqIdx) + '..' + str(endIdx)

                        data = [{
                            'id': foundSeqIdx,
                            'sequence': str(sequence_id),
                            'proteinName': str(protein_id),
                            'proteinLocation': str(formattedLocation),
                            'organism': str(rec.id)
                            }]
                        return JsonResponse(data, safe=False)
                else:
                    continue

        data = [{'id': -1, 'sequence': str(sequence_id)}]
        return JsonResponse(data, safe=False)


