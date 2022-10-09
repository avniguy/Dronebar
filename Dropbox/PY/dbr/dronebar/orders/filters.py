import django_filters
from django_filters import DateFilter,CharFilter,ChoiceFilter
from django import forms

from .models import *

from shops.models import Shop

# class OrderFilter(django_filters.FilterSet):
#
#     order_date = DateFilter(field_name="order_date",lookup_expr="gte")
#
#     class Meta:
#         model = Order
#         fields = '__all__'
#         exclude = ['items']

class OrderCreateFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields =  ['shop','customer']
        # exclude = ['shop','customer']
