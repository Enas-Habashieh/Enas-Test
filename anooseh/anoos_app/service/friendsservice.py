from anoos_app.models import EnasFriends, Country


def addfriendservice(request):
    friend = EnasFriends()
    friend.name = request.get('name')
    friend.mobile = request.get('mobile')
    friend.country_id = request.get('country_id')
    friend.save()
    return friend


def serviceupdateFriend(request, pk):
    friend = EnasFriends.objects.get(id=pk)
    friend.name = request.name
    friend.save()
    return friend


def deleteFriendsService(request, pk):
    try:
        friend = EnasFriends.objects.get(id=pk)
        friend.delete()
        return friend
    except EnasFriends.DoesNotExist:
        return None


def FriendsgetByIdService(request, pk):
    friend = EnasFriends.objects.get(id=pk)
    return friend


def FriendsgetAllService(request):
    friend = EnasFriends.objects.all()
    return friend


def updateparamfriendservice(request, pk):
    friend = EnasFriends.objects.get(id=pk)
    friend.name = request.GET.get('name', '')
    friend.save()
    return friend



