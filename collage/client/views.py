from django.shortcuts import render

from rest_framework.views import APIView

from .models import Client
from .serializers import ClientSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class ClientList(APIView):
    """
    List all clients
    """
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
