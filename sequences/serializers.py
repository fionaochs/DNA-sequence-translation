from rest_framework import serializers
from .models import Sequence, Result


class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Sequence

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'location',
        )
        model = Result