# Imports for Django views
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages
from .forms import *
from .models import *

# TEMPLATE VIEWS
def dashboard(request, pk_type=None, pk=None):
    inventories = Inventory.objects.all()
    shipments = Shipment.objects.all()

    inventory_instance = None
    shipment_instance = None

    if pk_type == "inventory" and pk:
        inventory_instance = Inventory.objects.get(pk=pk)
    elif pk_type == "shipment" and pk:
        shipment_instance = Shipment.objects.get(pk=pk)

    if request.method == "POST":
        form_id = request.POST.get("form_id")
        if form_id == "inventory-form":
            saveInventory(request, inventory_instance)
        elif form_id == "shipment-form":
            saveShipment(request, shipment_instance)
        return redirect('dashboard')

    inventory_form = InventoryForm(instance=inventory_instance)
    shipment_form = ShipmentForm(instance=shipment_instance)
    # print(inventory_instance)
    # print(shipment_instance)
    # shipment_form.fields["inventory"].queryset = shipment_instance.inventory_set if shipment_instance else None


    context = {
        'inventories':inventories,
        'shipments':shipments,
        'inventory_form': inventory_form,
        'shipment_form': shipment_form,
    }

    template_name = 'index.html'
    return render(request, template_name, context)


# ******************
# FORM HANDLERS
# ******************

# INVENTORY HANDLERS
def saveInventory(request, instance):
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=instance)
        if form.is_valid():
            item = form.save()
        else:
            print("Submission failed")
            messages.error(request, "Form submission failed")
    return

# SHIPMENT HANDLERS
def saveShipment(request, instance):
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=instance)
        if form.is_valid():
            item = form.save()
        else:
            print("Submission failed")
            messages.error(request, "Form submission failed")
    return

def deleteObject(request, pk_type, pk):
    obj = None
    if pk_type == "inventory":
        obj = Inventory.objects.get(pk=pk)
    elif pk_type == "shipment":
        obj = Shipment.objects.get(pk=pk)
    obj.delete()
    
    return redirect(request.META['HTTP_REFERER'])
