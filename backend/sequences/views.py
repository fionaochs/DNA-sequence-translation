from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from Bio.Seq import Seq
from Bio import SeqIO


# def ListFileSequences(request, sequence_id):
#     files = ['NC_000852.fasta', 'NC_009899.fasta', 'NC_008724.fasta', 'NC_007346.fasta','NC_014637.fasta','NC_020104.fasta','NC_023423.fasta','NC_023640.fasta','NC_023719.fasta','NC_027867.fasta']
#
#     for filename in files:
#         url = './organisms/{}'.format(filename)
#         record = SeqIO.read(url, "fasta")
#         seq = Seq(sequence_id)
#         genome = record.seq
#
#         foundSeqIdx = genome.find(sequence_id)
#
#         if foundSeqIdx != -1:
#             endIdx = foundSeqIdx + len(sequence_id)
#             formattedLocation = str(foundSeqIdx) + '..' + str(endIdx)
#             organismName = record.name
#             proteinName = seq.translate()
#
#             data = [{
#                     'id': foundSeqIdx,
#                     'sequence': str(sequence_id),
#                     'proteinName': str(proteinName),
#                     'proteinLocation': str(formattedLocation),
#                     'organism': str(organismName)
#                     }]
#             return JsonResponse(data, safe=False)
#         else:
#             continue
#
#     data = [{'id': -1, 'sequence': str(sequence_id)}]
#     return JsonResponse(data, safe=False)

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


# def genBankFile(request, sequence_id):
# #     for feature in gb_record.features:
#     foundSeqIdx = 1370
#     sequenceLength = foundSeqIdx + len(sequence_id)
#     for rec in SeqIO.parse("./organisms/NC_000852.gb","genbank"):
#         for feature in rec.features:
#              print('location ', feature.location.start.position)
#              print('location end ', feature.location)
#              startLocation = feature.location.start.position
#              endLocation = feature.location.end.position
#              if feature.type == "CDS" and (startLocation < foundSeqIdx and endLocation > sequenceLength):
#                 protein_id = feature.qualifiers["protein_id"][0]
#                 location = feature.location
#                 formattedLocation = str(foundSeqIdx) + '..' + str(endIdx)
#
#                 id = ">{} {} {}".format(rec.id, location, rec.description)
#                 print("{} \n {}".format(id, *protein_id))
# #                 return JsonResponse(str(feature), safe=False)
#                 data = [{
#                     'id': foundSeqIdx,
#                     'sequence': str(sequence_id),
#                     'proteinName': str(protein_id),
#                     'proteinLocation': str(feature.location),
#                     'organism': str(rec.id)
#                     }]
#                 return JsonResponse(data, safe=False)
# #                 return JsonResponse("{} \n {} {}".format(id, protein_id, startLocation), safe=False)
#     return JsonResponse(str(gb_record), safe=False)
