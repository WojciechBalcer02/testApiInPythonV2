from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Car

# Create your views here.
@csrf_exempt
def add_car(request):
    marka = request.POST.get('marka')
    model = request.POST.get('model')
    rok = request.POST.get('rok')
    car = Car(marka=marka, model=model, rok=rok)
    car.save()
    return HttpResponse("ustawiono")

def read_cars(request):
    cars = Car.objects.all()
    response = []
    for c in cars:
        response.append({"marka":c.marka, "model":c.model, "rok":c.rok})
    return JsonResponse(response, safe=False)
