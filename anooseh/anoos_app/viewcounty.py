from rest_framework.decorators import api_view
from rest_framework.response import Response

from anoos_app.controller.countrycontroller import countrydeletecontroller, addcountrycontroller
from anoos_app.serializer import CounrtrySerializer


@api_view(['POST'])
def addcountryview(request):
    response = addcountrycontroller(request)
    serializer = CounrtrySerializer(response)
    return Response(serializer.data)


@api_view(['DELETE'])
def countrydeleteview(request, pk):
    response = countrydeletecontroller(request, pk)
    if response is not None:
        return Response('deleted')
    else:
        return Response('not found')