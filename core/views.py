from re import T
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProposalListSerializer, ProposalCreateSerializer, ProposalSerializer
from .models import Proposal


class ProposalListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        proposals = Proposal.objects.all()
        proposals_json = ProposalListSerializer(proposals, many=True)
        return Response(data=proposals_json.data)


class ProposalCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = ProposalCreateSerializer(data=data)
        if serializer.is_valid():
            proposal = serializer.save()
            return Response(ProposalSerializer(instance=proposal).data, 201)
