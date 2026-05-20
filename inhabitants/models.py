from django.db import models
from rbi.models import *
from django.contrib.auth.models import User

class Households(models.Model):
    stat=[('yes','YES'),('no','NO')]
    sx=stat=[('M','MALE'),('F','FEMALE')]
    res=[('C','COMPLETED'),('CB','CALLBACK'),('R','REFUSED')]
    household_no=models.CharField(max_length=7,null=False,unique=True)
    household=models.CharField(max_length=10,choices=[('yes','YES'),('no','NO')],default='yes')
    ilq=models.CharField(max_length=10,choices=[('yes','YES'),('no','NO')],default='no')
    province=models.CharField(max_length=100,default='SULTAN KUDARAT')
    municipality=models.CharField(max_length=100,default='BAGUMBAYAN')
    barangay=models.ForeignKey(Barangay,on_delete=models.CASCADE,related_name='brgy')
    address=models.CharField(max_length=250,blank=True,default='')
    purok=models.CharField(max_length=250,default='')
    respondent=models.CharField(max_length=250)
    head=models.CharField(max_length=250)
    noofmembers=models.IntegerField()
    latitude=models.FloatField()
    longitude=models.FloatField()
    #B interview information
    dateofvisit1=models.DateField(blank=True,null=True)
    timestart1=models.TimeField(blank=True,null=True)
    timeend1=models.TimeField(blank=True,null=True)
    result1=models.CharField(max_length=10,choices=res,blank=True)
    datenextvisit1=models.DateField(blank=True,null=True)
    interviewer1=models.CharField( blank=True,max_length=250)
    supervisor1=models.CharField( blank=True,max_length=250)

    dateofvisit2=models.DateField(blank=True,null=True)
    timestart2=models.TimeField(blank=True,null=True)
    timeend2=models.TimeField(blank=True,null=True)
    result2=models.CharField(max_length=10,choices=res,blank=True)
    datenextvisit2=models.DateField(blank=True,null=True)
    interviewer2=models.CharField( blank=True,max_length=250)
    supervisor2=models.CharField( blank=True,max_length=250)
    #C Encoding Information
    dateencoded=models.DateField(blank=True,null=True)
    encoder=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    encodersupervisor=models.CharField(max_length=50,default='JHONG',blank=True,null=True)
  
    #HOUSEHOLD QUESTIONS
    Q45=models.IntegerField(blank=True,null=True,choices=[
          ('1','Rent-free without consent of owner'),('2','Rent-free with consent of owner'),('3','Rented'),('4','Owned/being amortized')])
    Q46=models.IntegerField(blank=True,null=True,choices=[
          ('1','Rent-free without consent of owner'),('2','Rent-free with consent of owner'),('3','Rented'),('4','Owned/being amortized')])
    Q47=models.IntegerField(blank=True,null=True,choices=[
         ('0','None'),('1','Oil(vegetable,animal,others)'),('2','Liquefied petroluem gas(LPG)'),('3','Kerosene(gaas)'),('4','Electricity'),('5','Others')])
    Q48=models.IntegerField(blank=True,null=True,choices=[
         ('0','None'),('1','Wood'),('2','Charcoal'),('3','Liquefied petroluem gas(LPG)'),('4','Kerosene(gaas)'),('5','Electricity'),('6','Others')])
    Q49=models.IntegerField(blank=True,null=True,choices=[
         ('1','Lake,river,rain,others'),('2','Dug well'),('3','Unprotected spring'),('4','Protected Spring'),('5','Peddler'),('6','Tubed/Piped shallow well'),
         ('7','Shared, faucet community water systemd'),('8','Own use/tubed/piped deep well'),('9','Shared, faucet community water system'),('10','Own use. faucet community water system'),('11','Bottled water'),('12','Others')])
    Q50A=models.IntegerField(blank=True,null=True,choices=[
         ('1','Feeding to animals'),('2','Burying'),('3','Composting'),('4','Burning'),('5','Dumping individual pit(not burned)'),('6','Picked-up by garbage truck')])
    Q50B=models.IntegerField(blank=True,null=True, choices=[('yes','YES'),('no','NO')])
    Q51=models.IntegerField(blank=True,null=True)
    Q52=models.IntegerField(blank=True,null=True)
    Q53=models.IntegerField(blank=True,null=True)
    Q54AGE=models.IntegerField(blank=True,null=True)
    Q54COD=models.CharField(max_length=100,blank=True,null=True)

    Q55AGE=models.IntegerField(blank=True,null=True)
    Q55SEX=models.CharField(max_length=100,blank=True,null=True,choices=sx)
    Q55COD=models.CharField(max_length=100,blank=True,null=True)
    q561=models.CharField(max_length=100,blank=True,null=True)
    q562=models.CharField(max_length=100,blank=True,null=True)
    q563=models.CharField(max_length=100,blank=True,null=True)

    q571=models.CharField(max_length=100,blank=True,null=True)
    q572=models.CharField(max_length=100,blank=True,null=True)
    q573=models.CharField(max_length=100,blank=True,null=True)

    q58b=models.CharField(max_length=100,blank=True,null=True)
    q58m=models.CharField(max_length=100,blank=True,null=True,default='BAGUMBAYAN')
    q58p=models.CharField(max_length=100,blank=True,null=True,default='SULTAN KUDARAT')

    



    

class Inhabitants(models.Model):
        hh=models.ForeignKey(Households,on_delete=models.CASCADE,related_name='household_inhabitants')
        lastname=models.CharField(max_length=100)
        firstname=models.CharField(max_length=100)
        middlename=models.CharField(max_length=100,blank=True)
        extname=models.CharField(max_length=100,blank=True)
        relationtohead=models.ForeignKey(Relationship,on_delete=models.SET_NULL,blank=True,null=True)
        sex=models.ForeignKey(Sex,on_delete=models.SET_NULL,blank=True,null=True)
        birthday=models.DateField(blank=True)
        bpcity=models.CharField(max_length=250,blank=True)
        bpprovince=models.CharField(max_length=250,blank=True)
        nationality=models.ForeignKey(Nationality,on_delete=models.SET_NULL,blank=True,null=True)
        maritalstatus=models.ForeignKey(MaritalStatus,on_delete=models.SET_NULL,blank=True,null=True)
        religion=models.ForeignKey(Religion,on_delete=models.SET_NULL,null=True,blank=True)
        etnicity=models.ForeignKey(Ethnicity,on_delete=models.SET_NULL,blank=True,null=True)
        highesteducation=models.ForeignKey(HighEducation,on_delete=models.SET_NULL,null=True,blank=True,default='')
        currentlyenrolled=models.ForeignKey(CurrentlyEnrolled,on_delete=models.SET_NULL,blank=True,null=True,default='')
        schoollevel=models.ForeignKey(SchoolLevel,on_delete=models.SET_NULL,blank=True,null=True,default='')
        placeofschool=models.CharField(max_length=250,blank=True,default='')

#economic activity

        monthlyincome=models.FloatField(default=0,blank=True)
        sourceofincome=models.ForeignKey(SourceIncome,on_delete=models.CASCADE,blank=True,null=True)
        statusofwork=models.ForeignKey(StatusWork,on_delete=models.CASCADE,null=True,blank=True)
        placeofwork=models.CharField(max_length=250,blank=True)
#healthinformation

        q19=models.ForeignKey(PlaceDelivery,on_delete=models.SET_NULL,blank=True,null=True)
        q20=models.CharField(max_length=250,blank=True,null=True)
        q21=models.CharField(max_length=250,blank=True,null=True)
        q22a=models.IntegerField(default=0,blank=True,null=True)
        q22b=models.IntegerField(default=0,blank=True,null=True)
        q23=models.ForeignKey(FPMethod,on_delete=models.SET_NULL,blank=True,null=True)
        q24=models.ForeignKey(SourceFP,on_delete=models.SET_NULL,blank=True,null=True)
        q25a=models.CharField(max_length=3,choices=[('yes','YES'),('no','NO')],default='no',blank=True,null=True)
        q25b=models.CharField(max_length=100,blank=True,null=True)
        q26=models.ForeignKey(HealthInsurance,on_delete=models.SET_NULL,blank=True,null=True)
        q27=models.ForeignKey(FacilityVisited,on_delete=models.SET_NULL,blank=True,null=True)
        q28=models.ForeignKey(ReasonVisit,on_delete=models.SET_NULL,blank=True,null=True)
        q29=models.CharField(max_length=100,blank=True,null=True)

#sociocivicparticipation
        q30=models.CharField(max_length=3,choices=[('1','1 REGISTERED SOLO PARENT'),('2','2 NON-SOLO PARENT'),('3','3 UNREGISTERED SOLO PARENT')],blank=True,null=True)
        Q31=models.CharField(max_length=3,choices=[('1','YES'),('2','NO')],blank=True,null=True)
        Q32=models.CharField(max_length=50,blank=True,null=True)

#migrationinformation

        q33a=models.CharField(max_length=50,blank=True,null=True)
        q33b=models.CharField(max_length=50,blank=True,null=True)
        q34a=models.CharField(max_length=50,blank=True,null=True)
        q34b=models.CharField(max_length=50,blank=True,null=True)
        q35a=models.IntegerField(default=0,blank=True,null=True)
        q35b=models.IntegerField(default=0,blank=True,null=True)
        q36=models.CharField(max_length=3,choices=[('1','1 NON-MIGRANT'),('2','2 MIGRANT'),('3','3 TRANSIENT'),('2','4 OFW')],blank=True,null=True)
        q37=models.DateField(blank=True,null=True)
        q38a=models.ForeignKey(ReasonsLeaving,on_delete=models.SET_NULL,blank=True,null=True,related_name='thirtya')
        q38b=models.ForeignKey(ReasonsLeaving,on_delete=models.SET_NULL,blank=True,null=True,related_name='thirtyb')
        q38c=models.ForeignKey(ReasonsLeaving,on_delete=models.SET_NULL,blank=True,null=True,related_name='thirtyc')
        q39a=models.CharField(max_length=3,choices=[('1','YES'),('2','NO')],blank=True,null=True)
        q39b=models.CharField(max_length=3,choices=[('1','YES'),('2','NO')],blank=True,null=True)
        q40a=models.ForeignKey(ReasonTransferring,on_delete=models.SET_NULL,blank=True,null=True,related_name='rft1')
        q40b=models.ForeignKey(ReasonTransferring,on_delete=models.SET_NULL,blank=True,null=True,related_name='rft2')
        q40c=models.ForeignKey(ReasonTransferring,on_delete=models.SET_NULL,blank=True,null=True,related_name='rft3')
        q41=models.CharField(max_length=50,blank=True,null=True)
#CTC
        q42a=models.CharField(max_length=3,choices=[('1','YES'),('2','NO')],blank=True,null=True)
        q42b=models.CharField(max_length=3,choices=[('1','YES'),('2','NO')],blank=True,null=True)

#SKILLS
        q43=models.CharField(max_length=250,blank=True,null=True)
        q44=models.ForeignKey(Skills,on_delete=models.SET_NULL,blank=True,null=True)
        class Meta:
              unique_together = ('hh', 'lastname', 'firstname', 'birthday')