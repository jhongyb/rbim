from django.shortcuts import render
from django.db.models import F,Count,Q
from django.contrib.auth.decorators import login_required
from rbi.models import Barangay
from inhabitants.models import Inhabitants
from rbi.access import userbrgy

@login_required()
def RBIbarangay(request):
    if request.user.username not in ["admin","mswd"]:
        inha=Barangay.objects.annotate(hh=Count('brgy',distinct=True),inh=Count('brgy__household_inhabitants',distinct=True)).filter(id__in=userbrgy(request.user))
    else:
        inha=Barangay.objects.annotate(hh=Count('brgy',distinct=True)
                                       ,inh=Count('brgy__household_inhabitants',distinct=True)
                                       ,prk=Count('brgy__purok',distinct=True))
    context={'inha':inha}
    return render(request,'barangay/barangay.html',context)

@login_required()
def RBIformc(request,b):
    brgy=Barangay.objects.all()
    context={'brgy':brgy}
    return render(request,'barangay/rbiformc.html')

@login_required()
def rbimindicators(request):
    brgy=Barangay.objects.all().order_by('id')
    if request.method=='POST':
        cri=request.POST['txtsearch']
        brgy=Barangay.objects.filter(Q(name__icontains=cri)).order_by('id')
    context={'brgy':brgy}
    return render(request,'barangay/indicators.html',context)

