from django.db.models import fields
from rest_framework import serializers
from .models import Proposal


class ProposalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'title']
