from django import forms
from .models import *
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'
    
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = "__all__"

class ShipmentForm(forms.ModelForm):
    shipment_date = forms.DateField(widget=forms.DateInput(attrs = {'value': datetime.now().strftime("%Y-%m-%d")}))
    
    class Meta:
        model = Shipment
        fields = "__all__"
