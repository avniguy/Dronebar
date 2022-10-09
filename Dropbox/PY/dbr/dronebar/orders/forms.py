from django import forms
from django.forms import modelformset_factory
from .models import Order,OrderRow
from shops.models import Shop

OrderRowFormSet = modelformset_factory(
    OrderRow, fields=( "item","quantity"), extra=1
)

class OrderModelForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

class ShopOptionForm(forms.Form):
    shops = Shop.objects.all()

    shop_select = list()
    shop_select.append(('-----','-----'))

    for s in shops:
        tuple1=(s.id,s.name)
        shop_select.append(tuple1)

    shop = forms.ChoiceField(choices=shop_select)
    user_id = forms.CharField(max_length=3,label="User Id", required=False)
