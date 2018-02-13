from rest_framework import serializers

from .models import Project
from account.serializers import AccountSerializer
from client.serializers import ClientSerializer


class ProjectSerializer(serializers.ModelSerializer):
    members = AccountSerializer(many=True, read_only=True, source='member')
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'client', 'members')
        depth = 3
