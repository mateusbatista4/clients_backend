from django.shortcuts import render
from rest_framework.response import Response

from .models import Member
from rest_framework import  viewsets
from .serializers import MemberSerializer, MemberMiniSerializer
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Member.objects.all()
        serializer = MemberMiniSerializer(queryset,many=True)
        return  Response(serializer.data)
