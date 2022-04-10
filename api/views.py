from rest_framework.response import Response
from rest_framework.decorators import api_view
from awwards.models import Projects
from .serializers import ProjectsSerializer


@api_view(['GET'])
def getData(request):
    '''
    API view functions for get request
    '''
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects, many=True)
    return Response(serializer.data)