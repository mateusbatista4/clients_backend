from django.shortcuts import render
from rest_framework.response import Response

from .models import Member
from rest_framework import  viewsets
from .serializers import MemberSerializer, MemberMiniSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request, *args, **kwargs):
        queryset = Member.objects.all()
        serializer = MemberMiniSerializer(queryset,many=True)
        return  Response(serializer.data)
