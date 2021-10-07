from django.shortcuts import render
from .models import carInstance, Car

def index(request):   
    cars_count = Car.objects.all().count()    
    
    num_cars_available = carInstance.objects.filter(status__exact = 'a').count()    

    cars = Car.objects.all()
    context = {
        'cars_count': cars_count,
        'num_cars_available': num_cars_available,
        'cars': cars,              
    }

    return render(request, 'index.html', context=context)

