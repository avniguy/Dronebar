from django.db import models
from shops.models import Menu, MenuItem , Shop #
from drones.models import Drone
from django.db.models.query import QuerySet
from django.utils import timezone

# Create your models here.

class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()

class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()

class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)

class Order(SoftDeletionModel):

    OrderStatus = (
        ('New',1),          # A new order which was not yet attended
        ('Processing',3),   # An order that is being prepared for shipping
        ('Shipped',4),      # An order which is on its way with a drone
        ('Delievered',5),   # An order which the consumer accepted with the app
        ('Closed',6),       # An order after delievered
        ('Canceled',7),     # Softly deleted order / canceled
    )

    customer = models.IntegerField()
    order_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 10, choices = OrderStatus, default = 1)
    shop = models.ForeignKey(Shop,on_delete=models.DO_NOTHING)
    drone = models.ForeignKey(Drone,on_delete=models.DO_NOTHING,null=True)
    total_price = models.FloatField(default=0)
    total_weight = models.FloatField(default=0)
    lat_location = models.FloatField(default=0)
    long_location = models.FloatField(default=0)


    def __str__(self):
        return "Order number:" + id + " , Total: " + total_price

class OrderRow(models.Model):
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    item = models.ForeignKey(MenuItem,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    item_price = models.FloatField(default=0)
    # item_weight = models.FloatField(default=0)

    def __str__(self):
        return "Order number:" + self.order.id

    # def get_absolute_url(self):
    #     return reverse("orders:order_detail",kwargs={"id":self.order_id})
