from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    industry_code = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'industry', 'code', 'industry_code')

    def get_industry_code(self, obj):
        return "INDUS-{}".format(obj.industry)