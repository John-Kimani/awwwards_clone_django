from rest_framework.response import Response
from rest_framework.decorators import api_view
from awwards.models import Projects
from members.models import Profile
from .serializers import ProjectsSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status

class ProjectsData(APIView):
    '''
    Class that provides pjoject data
    '''
    def get(self, request, format=None):
        '''
        API view function for get project data
        '''
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        '''
        API view function to post project data
        '''
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileData(APIView):
    '''
    Class that provides project data
    '''
    def get(self, request, format=None):
        '''
        API view function that get profile data
        '''
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        '''
        API view function to post profile data
        '''
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)