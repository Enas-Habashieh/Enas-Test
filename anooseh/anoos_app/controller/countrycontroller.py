from anoos_app.service.countryservice import addcountryservice, countrydeleteservice


def addcountrycontroller(request):
    data = request.data
    response = addcountryservice(data)
    return response


def countrydeletecontroller(request, pk):
    data = request.data
    response = countrydeleteservice(data, pk)
    return response
