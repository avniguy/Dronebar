from django import forms
from .models import DroneType, Drone


class DroneTypeModelForm(forms.ModelForm):
    class Meta:
        model = DroneType
        fields = '__all__'



class DroneModelForm(forms.ModelForm):
    class Meta:
        model = Drone
        fields = '__all__'
