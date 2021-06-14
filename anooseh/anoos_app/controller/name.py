from anoos_app.service.nameService import getservice, addnameservice


def addnamecontroller(request):
    data = request.data
    response = addnameservice(data)
    return response



def getcontroller(request,pk):
    response = getservice(request,pk)
    return response