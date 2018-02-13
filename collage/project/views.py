import time
from .models import Project
from .serializers import ProjectSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class ProjectList(APIView):
    """
    List all clients
    """
    def get(self, request, format=None):
        start = time.time()
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        data = serializer.data
        end = time.time()
        print("Took {}s".format(end - start))
        return Response(data)
