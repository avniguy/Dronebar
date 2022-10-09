from django.db import models
from django.urls import reverse
# from drones.models import DroneType

# Create your models here.


class ServiceSite(models.Model): #Locations where there is a drone service

    name = models.CharField(max_length=20,blank=False)
    description = models.CharField(max_length=50, blank=True)
    # gps_location = GpsLocation()
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    radius = models.IntegerField(default=10)

    # gps_location.SetLocation(1.0,1.0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shops:service_site_detail",kwargs={"id":self.id})

class ShopType(models.Model): # for future use

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class MenuItem(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    weight = models.IntegerField()
    price = models.FloatField(default=0)
    # menu = models.ManyToManyField(Menu)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shops:menu_item_detail",kwargs={"id":self.id})

class Menu(models.Model):

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shops:menu_detail",kwargs={"id":self.id})

class Shop(models.Model):

    name = models.CharField(max_length=25)
    description = models.CharField(blank=True, max_length=50)
    address = models.CharField(max_length=50)
    # drone_type = models.ForeignKey(DroneType,related_name='shop_drone_type',default=1,on_delete=models.DO_NOTHING)
    active = models.BooleanField(blank=False,default=False)
    service_site = models.ForeignKey(ServiceSite,related_name='Shops',null=True,on_delete=models.DO_NOTHING)
    menu = models.ForeignKey(Menu,related_name='menu',null=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shops:shop_detail",kwargs={"id":self.id})


# class ContractType(models.Model):
#     name = models.CharField(max_length=25)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name
#
# class Contract(models.Model):
#     shop = models.ForeignKey(Shop,related_name="shop_id",on_delete=models.DO_NOTHING)
#     contract_type = models.ForeignKey(ContractType,related_name="conract_type",on_delete=models.DO_NOTHING)
#     price = models.FloatField()
#
#     def __str__(self):
#         return "Contract for shop:" + self.shop + " and contract type: " + self.contract_type + " and price=" + self.price

# class MenuItemPrice(models.Model):
#
#     shop = models.ForeignKey(Shop,related_name="shop",on_delete=models.CASCADE)
#     item = models.ForeignKey(MenuItem,related_name="item",on_delete=models.CASCADE)
#     price = models.FloatField(null=False)
#
#     def __str__(self):
#         return "shop:" + self.shop + ", item:" + self.item + ",price:" + self.price
