from rest_framework import serializers
from .models import Sequence


class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Sequence
