from anoos_app.models import Country


def addcountryservice(request):
    country = Country()
    country.name = request.get('name')
    country.save()
    return country


def countrydeleteservice(request, pk):
    try:
        country = Country.objects.get(id=pk)
        country.delete()
        return country
    except Country.DoesNotExist:
        return None
