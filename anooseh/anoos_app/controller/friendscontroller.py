from anoos_app.dto.request.request import FriendsRequest
from anoos_app.service.friendsservice import addfriendservice, serviceupdateFriend, deleteFriendsService, \
    FriendsgetByIdService, FriendsgetAllService, updateparamfriendservice


def addfriendcontroller(request):
    data = request.data
    response = addfriendservice(data)
    return response


def controllerupdateFriend(request, pk):
    data = request.data
    data1 = FriendsRequest(data)
    response = serviceupdateFriend(data1, pk)
    return response


def deleteFriendsController(request, pk):
    data = request.data
    response = deleteFriendsService(data, pk)
    return response


def FriendsgetByIdController(request, pk):
    response = FriendsgetByIdService(request, pk)
    return response


def FriendsgetAllcontroller(request):
    response = FriendsgetAllService(request)
    return response


def updateparamfriendcontroller(request, pk):
    response = updateparamfriendservice(request, pk)
    return (response)
