from __future__ import absolute_import, unicode_literals
import celery
import os
from django.http import HttpResponse, JsonResponse
from Bio.Seq import Seq
from Bio import SeqIO
from celery import shared_task

app = celery.Celery('sequences_api')

app.conf.update(BROKER_URL='redis://:p6595a4738e2f311e89507baec7e0e2137ff1427ebe650054c79471d49f8d3e83@ec2-3-218-1-197.compute-1.amazonaws.com:10719',
                CELERY_RESULT_BACKEND='redis://:p6595a4738e2f311e89507baec7e0e2137ff1427ebe650054c79471d49f8d3e83@ec2-3-218-1-197.compute-1.amazonaws.com:10719')

@app.task
def add(x, y):
    return x+y


@shared_task(bind=True)
def findProtein(self, sequence_id):
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
                            return data
                    else:
                        continue

            data = [{'id': -1, 'sequence': str(sequence_id)}]
            return data