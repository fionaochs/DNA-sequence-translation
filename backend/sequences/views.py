from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from Bio.Seq import Seq
from Bio import SeqIO, SeqFeature


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



def genBankFile(request, sequence_id):
#     for feature in gb_record.features:
    foundSeqIdx = 1370
    sequenceLength = foundSeqIdx + len(sequence_id)
    for rec in SeqIO.parse("./organisms/NC_000852.5.gb","genbank"):
        for feature in rec.features:
             print('location ', feature.location.start.position)
             print('location end ', feature.location.end.position)
             startLocation = feature.location.start.position
             endLocation = feature.location.end.position
             if feature.type == "CDS" and (startLocation < foundSeqIdx and endLocation > sequenceLength):
                seq = feature.qualifiers["protein_id"][0]
                location = feature.location
                id = ">{} {} {}".format(rec.id, location, rec.description)
                print("{} \n {}".format(id, *seq))
                return JsonResponse(str(feature), safe=False)
#                 return JsonResponse("{} \n {} {}".format(id, *seq, startLocation), safe=False)
    return JsonResponse(str(gb_record), safe=False)

def exampleFile(request, sequence_id):
    gbank = SeqIO.parse("./organisms/NC_000852.5.gb", 'genbank')
    for genome in gbank:
        print(f'looking in %{genome.id}')
        for gene in genome.features:
            if gene.type == 'CDS':
               return JsonResponse(str(gene), safe=False)
