from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
import uuid
from phonenumber_field.modelfields import PhoneNumberField

class CarOwner(models.Model):
    """Model that represents car owner"""

    first_name = models.CharField(
        'First Name', max_length=15, help_text='Please enter first name')
    last_name = models.CharField(
        'Last Name', max_length=15, help_text='Please enter last name')
    national_id_number = models.CharField(
        'National ID', max_length=8, null=False, blank=False,
        unique=True, help_text='Please enter National ID number')
    phone = PhoneNumberField('Phone Number', null=False, blank=False,
                             unique=True, help_text='Please enter phone number')    

    def __str__(self):
        return (f'{self.national_id_number} {self.first_name} {self.last_name}')

#First model
class CarType(models.Model):
    #heredoc
    """ Model that represents the car type """
    car_type = models.CharField(max_length = 200, help_text = 'Please enter car type (e.g. SUV, Saloon...)')

    def __str__(self):
        return self.car_type

#Second model
class CarMake(models.Model):
    """Model that represent a car make"""
    #'Make' is a verbose_name
    car_make = models.CharField('Make', max_length = 200, help_text = 'Please enter car make (e.g. Toyota, Nissan...)')

    def __str__(self):
        return self.car_make

#Third model
class CarModel(models.Model):
    """Model that represents car model"""

    car_model = models.CharField('Model', max_length = 200, help_text = 'Please enter car model (e.g. Corolla, Sunny...)')

    def __str__(self):
        return self.car_model

#Forth model
class Car(models.Model):
    """Model that represents a car"""
    registration = models.CharField('Reg No.', max_length = 8, unique = True)
    car_owner = models.ForeignKey(CarOwner, on_delete=models.RESTRICT, null=True, blank=True,)
    car_type = models.ForeignKey(CarType, on_delete = models.RESTRICT)
    car_make = models.ForeignKey(CarMake, on_delete = models.RESTRICT)
    car_model = models.ForeignKey(CarModel, on_delete = models.RESTRICT)
    description = models.TextField(max_length = 1000, help_text = "Some additional info about the car")    
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return  (f'{self.car_make} {self.car_model} {self.registration}')

    #reverse the object to generate a URL to the string output
    def get_absolute_url (self):
        # returns a URL to generate a detailed car record
        return reverse('car-detail', args=[str(self.id)])

# Added this class
class CarImage(models.Model):    
    # ForeignKey field refering to the Car class
    car = models.ForeignKey(Car, default=None, on_delete=models.RESTRICT)
    # Field for uploading multiple images
    image = models.ImageField(upload_to = 'images/')
 
    def __str__(self):
        return  (f'{self.car.car_make} {self.car.car_model} {self.car.registration}')

class carInstance(models.Model):
    """Model to represent a car instance"""

    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    car = models.ForeignKey('Car', on_delete = models.RESTRICT, null = True)
    imprint = models.CharField(max_length = 500)
    due_back = models.DateField(null = True, blank = True) 

    hire_status = (
        ('a', 'Available'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
        ('m', 'Maintenance'),
    )

    status = models.CharField(
        max_length = 1,
        choices = hire_status,
        blank = True,
        default = 'a',
        help_text = 'Car Availability'  
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} {self.car}'


    

