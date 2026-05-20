from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rbi.models import Barangay

@login_required()
def RBIbarangay(request):
    brgy=Barangay.objects.all().order_by('name')
    context={'brgy':brgy}
    return render(request,'barangay/barangay.html',context)

@login_required()
def RBIformc(request,b):
    brgy=Barangay.objects.all()
    context={'brgy':brgy}
    return render(request,'barangay/rbiformc.html')

