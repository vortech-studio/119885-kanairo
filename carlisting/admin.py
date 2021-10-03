from django.contrib import admin
from .models import CarType, CarMake, CarModel, carInstance, Car,  CarOwner, CarImage   

class CarInline(admin.TabularInline):
    model = Car

class CarOwnerAdmin(admin.ModelAdmin):
    inlines = [
        CarInline,
    ]

# Added this section
# # # # # # # # # # # # # # # # # # # # # 
class CarImageInline(admin.StackedInline):
    model = CarImage
 
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
 
    class Meta:
       model = Car
# # # # # # # # # # # # # # # # # # # # # 
 


#Register the models here

admin.site.register(CarType)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(carInstance)
admin.site.register(CarOwner)






