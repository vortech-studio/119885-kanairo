from django.contrib import admin
from .models import CarType, CarMake, CarModel, carInstance, Car,  CarOwner, CarImage   

class CarInline(admin.TabularInline):
    model = Car

class CarOwnerAdmin(admin.ModelAdmin):
    inlines = [
        CarInline,
    ]

# Add multiple images for a vehicle
# # # # # # # # # # # # # # # # # # # # # 
class CarImageAdmin(admin.StackedInline):
    model = CarImage
 
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageAdmin]
 
    class Meta:
       model = Car

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    pass
# # # # # # # # # # # # # # # # # # # # # 
 


#Register the models here

admin.site.register(CarType)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(carInstance)
admin.site.register(CarOwner)






