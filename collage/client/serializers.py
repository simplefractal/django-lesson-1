from rest_framework import serializers

from .models import Client
from task.models import Task


class ClientSerializer(serializers.ModelSerializer):
    industry_code = serializers.SerializerMethodField(read_only=True)
    needs_attention = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Client
        fields = (
            'id', 'name', 'email', 'industry', 'code', 'industry_code', 'needs_attention')

    def get_industry_code(self, obj):
        return "INDUS-{}".format(obj.industry)

    def get_needs_attention(self, obj):
        tasks = Task.objects.filter(client=obj)
        for task in tasks:
            names = task.tags.values_list('name', flat=True)
            if 'Urgent' in names:
                return True
        return False