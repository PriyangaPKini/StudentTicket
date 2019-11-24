from django.shortcuts import render,redirect

from .models import Complaint


# Create your views here.
def complaint(request):
    if request.method == 'POST':

        busNumber = request.POST['busNumber']
        message = request.POST['message']

        complaint = Complaint( busNumber=busNumber, message=message)
        complaint.save()

        return redirect('')