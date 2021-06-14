from anoos_app.models import Names


def addnameservice(request):
    names = Names()
    names.name = request.get('name')
    names.last = request.get('last')
    names.save()
    return names


def getservice(request, pk):
    names = Names.objects.get(id=pk)
    return names
