from rest_framework.response import Response
from rest_framework.decorators import api_view
from awwards.models import Projects
from .serializers import ProjectsSerializer


@api_view(['GET'])
def getData(request):
    '''
    API view function for get project data
    '''
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    '''
    API view function to post project data
    '''
    serializer = ProjectsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)