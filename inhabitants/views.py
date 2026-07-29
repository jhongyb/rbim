from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import HouseholdForm,Inhabitants_InlineForm
from django.contrib import messages
from .models import Households,Barangay,Inhabitants
from django.db import transaction
from django.db.models import Q,F
from rbi.access import barangay_access,userbrgy


@login_required
@barangay_access(redirect_url='/home')
def households(request):
    # print(userbrgy(request.user))
    return render(request,'households/household.html')

@login_required
@barangay_access(redirect_url='/home')
def newhouseholds(request):
    if request.method=='POST':
        data=request.POST
        try:
            Households.objects.create(
                household_no=data['household_no'],
                household=data['household'],
                ilq=data['ilq'],
                province=data['province'],
                municipality=data['municipality'],
                barangay=Barangay.objects.get(id=data['barangay']),
                address=data['address'],
                purok=data['purok'],
                respondent=data['respondent'],
                head=data['head'],
                noofmembers=data['noofmembers'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                encoder=request.user
                )
            messages.success(request,'Household Successfully Save.')
            return redirect('householdlist')
        except Exception as e:
            messages.error(request,e)
            return redirect('householdlist')
    else:
        form=HouseholdForm()
        return render(request,'households/newhousehold.html',{'form':form,'barangay':userbrgy(request.user)})

@login_required
def household_update(request,pk):
    data=Households.objects.get(id=pk)
    if request.method=='POST':
        form=HouseholdForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Household Successfully Updated!')
            return redirect('householdlist')
    form=HouseholdForm(instance=data)
    return render(request,'households/updatehousehold.html',{'form':form})

@login_required
def household_delete(request,pk):
    data=Households.objects.get(id=pk)
    if data:
        data.delete()
        messages.success(request,'Household Successfully Deleted!')
        return redirect('householdlist')
    else:
        messages.error(request,'Household Not Successfully Deleted!')
        return redirect('householdlist')


@login_required
def householdlist(request):
    data=Households.objects.all()
    if request.user.username not in ["admin","mswd"]:
        b=userbrgy(request.user)
        data=Households.objects.filter(barangay__in=b)
        if request.method=='POST':
            cri=request.POST['txtsearch']
            data=Households.objects.filter(Q(household_no__icontains=cri)|Q(head__icontains=cri)|Q(purok__icontains=cri),barangay__in=b)
    else:
        if request.method=='POST':
                cri=request.POST['txtsearch']
                data=Households.objects.filter(Q(household_no__icontains=cri)|Q(head__icontains=cri)|Q(purok__icontains=cri))
    return render(request,'households/householdlist.html',{'data':data})

@login_required
def inhabitantslist(request):
    if request.user.username not in ["admin","mswd"]:
        data=Inhabitants.objects.select_related('hh').annotate(
                                        hhno=F('hh__household_no'),sx=F('sex__description'),purok=F('hh__purok')
                                        ,brgy=F('hh__barangay__name'),brgyid=F('hh__barangay__id'),pk=F('pk')).values('pk',
                                        'lastname','firstname','middlename','hhno','sx','purok','brgy',
                                        'extname','birthday').order_by('hhno').filter(brgyid__in=userbrgy(request.user))
        brgy=Barangay.objects.all()
        if request.method=='POST':
            cri=request.POST['txtsearch']
            data=Inhabitants.objects.select_related('hh').annotate(
                                        hhno=F('hh__household_no'),sx=F('sex__description'),purok=F('hh__purok')
                                        ,brgy=F('hh__barangay__name'),brgyid=F('hh__barangay__id'),pk=F('pk')).values('pk',
                                        'lastname','firstname','middlename','hhno','sx','purok','brgy',
                                        'extname','birthday').order_by('hhno').filter(
                                            Q(hhno__icontains=cri)|Q(lastname__icontains=cri)|Q(purok__icontains=cri)
                                            |Q(firstname__icontains=cri)|Q(middlename__icontains=cri),brgyid__in=userbrgy(request.user))
    else:
        data=Inhabitants.objects.select_related('hh').annotate(
                                        hhno=F('hh__household_no'),sx=F('sex__description'),purok=F('hh__purok')
                                        ,brgy=F('hh__barangay__name'),brgyid=F('hh__barangay__id'),pk=F('pk')).values('pk',
                                        'lastname','firstname','middlename','hhno','sx','purok','brgy',
                                        'extname','birthday').order_by('hhno')
        brgy=Barangay.objects.all()
        if request.method=='POST':
            cri=request.POST['txtsearch']
            data=Inhabitants.objects.select_related('hh').annotate(
                                        hhno=F('hh__household_no'),sx=F('sex__description'),purok=F('hh__purok')
                                        ,brgy=F('hh__barangay__name'),brgyid=F('hh__barangay__id'),pk=F('pk')).values('pk',
                                        'lastname','firstname','middlename','hhno','sx','purok','brgy',
                                        'extname','birthday').order_by('hhno').filter(
                                            Q(hhno__icontains=cri)|Q(lastname__icontains=cri)|Q(purok__icontains=cri)
                                            |Q(firstname__icontains=cri)|Q(middlename__icontains=cri))
    return render(request,'households/inhabitantslist.html',{'data':data,'brgy':brgy})

@login_required
def inhabitant_members(request,pk):
# 1. Use get_object_or_404 for better error handling
    hh = get_object_or_404(Households, household_no=pk)
    if request.method == 'POST':
        # 2. Bind the POST data to the formset
        formset = Inhabitants_InlineForm(request.POST,request.FILES, instance=hh)
        if formset.is_valid():
            try:
                # 3. Use a transaction to ensure all members save or none do
                with transaction.atomic():
                    formset.save()
                messages.success(request, 'Household members updated successfully!')
                return redirect('inhabitants', pk=pk)
            except Exception as e:
                messages.error(request, f'Database Error: {str(e)}')
        else:
            # If invalid, it will fall through to the render below and show errors
            messages.error(request, 'Please correct the errors in the form.')
    else:
        # 4. GET request: just show the existing data
        formset = Inhabitants_InlineForm(instance=hh)
        
    return render(request, 'households/inhabitants.html', {
        'formset': formset,
        'hh': hh
    })