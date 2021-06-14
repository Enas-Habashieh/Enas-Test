from django.shortcuts import render

# Create your views here.
from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.response import Response

from anoos_app.controller.countrycontroller import addcountrycontroller, countrydeletecontroller
from anoos_app.controller.friendscontroller import addfriendcontroller, controllerupdateFriend, deleteFriendsController, \
    FriendsgetByIdController, FriendsgetAllcontroller, updateparamfriendcontroller
from anoos_app.controller.name import addnamecontroller, getcontroller
from anoos_app.dto.response.nameResponse import namesresponse
from anoos_app.dto.response.response import friendsGetbyidResponse
from anoos_app.dto.response.responseadd import friendaddResponse
from anoos_app.serializer import FriendSerializer, CounrtrySerializer, NamesSerializer


@api_view(['POST'])
def addfreiendview(request):
    response = addfriendcontroller(request)
    response1 = friendaddResponse(response)
   # serializer = FriendSerializer(response)
    return Response(response1)


@api_view(['POST'])
def viewupdateFriend(request, pk):
    response = controllerupdateFriend(request, pk)
    serializer = FriendSerializer(response)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteFriendView(request, pk):
    response = deleteFriendsController(request, pk)
    if response != None:
        return Response('deleted')
    else:
        return Response('not found')
    return response


@api_view(['GET'])
def FriendsgetByIdview(request, pk):
    response = FriendsgetByIdController(request, pk)
    response1 = friendsGetbyidResponse(response)
    #serializer = FriendSerializer(response, many=False)
    return Response(response1)


@api_view(['GET'])
def FriendsgetAllView(request):
    response = FriendsgetAllcontroller(request)
    serializer=FriendSerializer(response, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def updateparamfriendview(request, pk):
    response = updateparamfriendcontroller(request, pk)
    serializer = FriendSerializer(response)
    return Response(serializer.data)




###################
@api_view(['POST'])
def addnameview(request):
    response = addnamecontroller(request)
    serializer = NamesSerializer(response)
    return Response(serializer.data)


@api_view(['GET'])
def getview(request, pk):
    response = getcontroller(request, pk)
    response1 = namesresponse(response)
    # serializer = FriendSerializer(response, many=False)
    return Response(response1)