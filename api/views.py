from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    '''
    API view functions for get request
    '''
    project = {'name': 'Moana', 'design':30}
    return Response(project)