from django.db import models

# Create your models here.
class FarmerData(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    coffee_ammount = models.CharField(max_length=20)
    coffee_type = models.CharField(max_length=20)


    def __str__(self):
        return self.name
    
class TourismSpot(models.Model):
    image = models.ImageField(upload_to='tourism/images/')
    area_found = models.CharField(max_length=100 )
    distance_from_addis = models.CharField(max_length=100)

    def __str__(self):
        return self.area_found     