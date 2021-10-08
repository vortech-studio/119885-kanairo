from django.shortcuts import render
from .models import carInstance, Car, CarImage

def index(request):   
    
    num_cars_available = carInstance.objects.filter(status__exact = 'a').count()    
    cars_list=[]      

    cars = Car.objects.all()
    for car in cars:
        images_list=[]
        images = list(CarImage.objects.filter(car=car))
        for image in images:
            images_list.append(image.image.url)
        car_object = {
            'model':car.car_model,
            'make':car.car_make,
            'type':car.car_type,
            'registration':car.registration,
            'description':car.description,
            'images':images_list,
        }    
        cars_list.append(car_object)
         
    context = {        
        'num_cars_available': cars.count(),
        'cars': cars_list,            
    }

    return render(request, 'index.html', context=context)

