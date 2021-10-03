from django.shortcuts import render
from .models import carInstance, Car

def index(request):   
    cars_count = Car.objects.all().count()
    car_instance_count = carInstance.objects.all().count()
    
    num_cars_available = carInstance.objects.filter(status__exact = 'a').count()

    number_of_visits = request.session.get('number_of_visits', 0)
    request.session['number_of_visits'] = number_of_visits + 1

    context = {
        'cars_count': cars_count,
        'num_cars_available': num_cars_available,
        'car_instance_count': car_instance_count,
        'number_of_visits': number_of_visits,        
    }

    return render(request, 'index.html', context=context)

