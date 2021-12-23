from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from Bio.Seq import Seq
from Bio import SeqIO


def ListFileSequences(request, sequence_id):
    files = ['NC_000852.fasta', 'NC_009899.fasta', 'NC_008724.fasta', 'NC_007346.fasta','NC_014637.fasta','NC_020104.fasta','NC_023423.fasta','NC_023640.fasta','NC_023719.fasta','NC_027867.fasta']

    for filename in files:
        url = './organisms/{}'.format(filename)
        record = SeqIO.read(url, "fasta")
        seq = Seq(sequence_id)
        genome = record.seq

        foundSeqIdx = genome.find(sequence_id)

        if foundSeqIdx != -1:
            endIdx = foundSeqIdx + len(sequence_id)
            formattedLocation = str(foundSeqIdx) + '..' + str(endIdx)
            organismName = record.name
            proteinName = seq.translate()

            data = [{
                    'id': foundSeqIdx,
                    'sequence': str(sequence_id),
                    'proteinName': str(proteinName),
                    'proteinLocation': str(formattedLocation),
                    'organism': str(organismName)
                    }]
            return JsonResponse(data, safe=False)
        else:
            continue

    data = [{'id': -1, 'sequence': str(sequence_id)}]
    return JsonResponse(data, safe=False)
