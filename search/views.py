from car.models import carName
# Create your views here.

from django.shortcuts import render,render_to_response

def index(request):
    return render_to_response('search.html')

def searchResults(request):
    crname = request.GET.get('crname')
    cars = carName.objects.filter(name__contains=crname)
    print cars
    #return render_to_response('searchresults.html',cars)
    context = {
     "cars" : cars,}
    return render(request,"searchresults.html",context) 
