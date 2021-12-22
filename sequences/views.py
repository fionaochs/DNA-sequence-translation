from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from Bio.Seq import Seq
from Bio import SeqIO


def ListFileSequences(request, sequence_id):
#  'CGCAGGCGCT'
#  'AAGGTCGCCTCGGTGTC'
    files = ['NC_000852.fasta', 'NC_009899.fasta', 'NC_008724.fasta', 'NC_007346.fasta','NC_014637.fasta','NC_020104.fasta','NC_023423.fasta','NC_023640.fasta','NC_023719.fasta','NC_027867.fasta']

    for filename in files:
        url = '/Users/fiona.ochs/Documents/Projects/sequenceDNA/organisms/{}'.format(filename)
        record = SeqIO.read(url, "fasta")
        upperCaseStrId = sequence_id.upper()
        seq = Seq(upperCaseStrId)
        genome = record.seq

        foundSeqIdx = genome.find(sequence_id) # 1370

        if foundSeqIdx != -1:
            endIdx = foundSeqIdx + len(sequence_id)
            formattedLocation = str(foundSeqIdx) + '..' + str(endIdx) # 1370..1380
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
    print(data)
    return JsonResponse(data, safe=False)

# def genBankFile(request, sequence_id):
# #     gb_record = SeqIO.read("/Users/fiona.ochs/Documents/Projects/sequenceDNA/sequence.gb","genbank")
# #     for feature in gb_record.features:
#     foundSeqIdx = 1370
#     for rec in SeqIO.parse("/Users/fiona.ochs/Documents/Projects/sequenceDNA/sequence.gb","genbank"):
#         for feature in rec.features:
#              startLocation = '{}'.format(feature.location)[1:].partition(':')[0]
# #              startLocation = '{}'.format(feature.location)[1:].partition(':')[0]
#              if feature.type == "CDS" and int(startLocation) < foundSeqIdx:
#                 seq = feature.qualifiers["protein_id"]
#                 location = feature.location
#                 id = ">{} {} {}".format(rec.id, location, rec.description)
#                 print("{} \n {}".format(id, *seq))
#                 return JsonResponse("{} \n {} {}".format(id, *seq, startLocation), safe=False)
#     return JsonResponse(str(gb_record), safe=False)
# ID: NC_000852.5
# Name: NC_000852.5
# Description: NC_000852.5 Paramecium bursaria Chlorella virus 1, complete genome
# Number of features: 0
# Seq('GGGAGAACCAGGTGGGATTGACAGTGGTAAATGTGTTGACCACGAGTAAAAACA...TTT')
# filter Seq object for sequence