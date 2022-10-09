from django.db import models
from django.urls import reverse
from shops.models import Shop


# Create your models here.
class DroneType(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    self_weight = models.IntegerField()
    payload_weight = models.IntegerField()
    external_reference = models.CharField(max_length=25,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("drones:drone_type_detail",kwargs={"id":self.id})



class Drone(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    drone_type = models.ForeignKey(DroneType,related_name="drone_type",on_delete=models.DO_NOTHING)
    shop = models.ForeignKey(Shop,related_name="shop",on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("drones:drone_detail",kwargs={"id":self.id})
