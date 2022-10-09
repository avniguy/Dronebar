from django import forms
from .models import Shop,ServiceSite, Menu, MenuItem #


class ShopModelForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name',
                  'description',
                  'address',
                  'active',
                  'service_site',
                  # 'drone_type',
                  'menu',
        ]


class ServiceSiteModelForm(forms.ModelForm):
    class Meta:
        model = ServiceSite
        fields = '__all__'


class MenuModelForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuItemModelForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"
