from django import forms
from .models import Households,Inhabitants
from django.forms import inlineformset_factory

class HouseholdForm(forms.ModelForm):
    class Meta:
        model=Households
        fields='__all__'
        labels={
            'ilq':"Institutional Living Quarter",
            'address':"Address (Room/Floor/Unit No. and Building Name) (House/Lot and Block No.)",
            'dateofvisit1':'','dateencoded':'','encoder':'','encodersupervisor':'',
            'timestart1':'',
            'timeend1':'',
            'result1':'',
            'datenextvisit1':'',
            'interviewer1':'',
            'supervisor1':'','supervisor2':'',
            'dateofvisit2':'',
            'timestart2':'',
            'timeend2':'',
            'result2':'',
            'datenextvisit2':'',
            'interviewer2':'',
            
            'Q45':'', 'Q47':'','Q48':'','Q49':'','Q50A':'','Q50B':'','Q51':'','Q52':'','Q46':'','Q53':'','Q54AGE':'','Q54COD':'',
            'Q55AGE':'','Q55SEX':'','Q55COD':'','q561':'','q562':'','q563':'','q571':'','q572':'','q573':''
            ,'q58b':'','q58m':'','q58p':''
            }
        widgets={
            'dateencoded':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'timestart1':forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'timeend1':forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'dateofvisit1':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'datenextvisit1':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'timestart2':forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'timeend2':forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'dateofvisit2':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'datenextvisit2':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'Q54AGE':forms.TextInput(attrs={'placeholder':'Age'}),
            'Q54COD':forms.TextInput(attrs={'placeholder':'Cause of Death'}),
            'Q55AGE':forms.TextInput(attrs={'placeholder':'Age'}),
            'Q55SEX':forms.TextInput(attrs={'placeholder':'Sex'}),
            'Q55COD':forms.TextInput(attrs={'placeholder':'Cause of Death'}),

            'q561':forms.TextInput(attrs={'placeholder':'1'}),
            'q562':forms.TextInput(attrs={'placeholder':'2'}),
            'q563':forms.TextInput(attrs={'placeholder':'3'}),
            'q571':forms.TextInput(attrs={'placeholder':'1'}),
            'q572':forms.TextInput(attrs={'placeholder':'2'}),
            'q573':forms.TextInput(attrs={'placeholder':'3'}),

            'q58b':forms.TextInput(attrs={'placeholder':'Barangay'}),
            'q58m':forms.TextInput(attrs={'placeholder':'Municipality'}),
            'q58p':forms.TextInput(attrs={'placeholder':'Province'}),
            


        }
class InhabitantsForm(forms.ModelForm):
     class Meta:
        model=Inhabitants
        fields='__all__'
        widgets={
            'birthday':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'middlename':forms.TextInput(attrs={'class':'form-control'}),
            'extname':forms.TextInput(attrs={'class':'form-control'}),
            'relationtohead':forms.Select(attrs={'class':'form-select'}),
            'sex':forms.Select(attrs={'class':'form-select'}),
            'bpcity':forms.TextInput(attrs={'class':'form-control','placeholder':'Municipality / City'}),
            'bpprovince':forms.TextInput(attrs={'class':'form-control','placeholder':'Province'}),
            'nationality':forms.Select(attrs={'class':'form-select'}),
            'maritalstatus':forms.Select(attrs={'class':'form-select'}),
            'etnicity':forms.Select(attrs={'class':'form-select'}),
            'currentlyenrolled':forms.Select(attrs={'class':'form-select'}),
            'schoollevel':forms.Select(attrs={'class':'form-select'}),
            'maritalstatus':forms.Select(attrs={'class':'form-select'}),
            'religion':forms.Select(attrs={'class':'form-select'}),
            'highesteducation':forms.Select(attrs={'class':'form-select'}),
            'placeofschool':forms.TextInput(attrs={'class':'form-control'}),
            'monthlyincome':forms.TextInput(attrs={'class':'form-control'}),
            'placeofwork':forms.TextInput(attrs={'class':'form-control'}),
            'sourceofincome':forms.Select(attrs={'class':'form-select'}),
            'statusofwork':forms.Select(attrs={'class':'form-select'}),
            'q19':forms.Select(attrs={'class':'form-select'}),
            'q20':forms.TextInput(attrs={'class':'form-control'}),
            'q21':forms.TextInput(attrs={'class':'form-control'}),
            'q22a':forms.TextInput(attrs={'class':'form-control','placeholder':'No of Pregnancies'}),
            'q22b':forms.TextInput(attrs={'class':'form-control','placeholder':'No of still living'}),
            'q23':forms.Select(attrs={'class':'form-select'}),
            'q24':forms.Select(attrs={'class':'form-select'}),
            'q25a':forms.Select(attrs={'class':'form-select'}),
            'q25b':forms.TextInput(attrs={'class':'form-control'}),
            'q26':forms.Select(attrs={'class':'form-select'}),
            'q27':forms.Select(attrs={'class':'form-select'}),
            'q28':forms.Select(attrs={'class':'form-select'}),
            'q29':forms.TextInput(attrs={'class':'form-control'}),
            'q30':forms.Select(attrs={'class':'form-select'}),
            'Q31':forms.Select(attrs={'class':'form-select'}),
            'Q32':forms.TextInput(attrs={'class':'form-control'}),
            'q33a':forms.TextInput(attrs={'class':'form-control'}),
            'q33b':forms.TextInput(attrs={'class':'form-control'}),
            'q34a':forms.TextInput(attrs={'class':'form-control'}),
            'q34b':forms.TextInput(attrs={'class':'form-control'}),
            'q35a':forms.TextInput(attrs={'class':'form-control'}),
            'q35b':forms.TextInput(attrs={'class':'form-control'}),
            'q36':forms.Select(attrs={'class':'form-select'}),
            'q37':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'q38a':forms.Select(attrs={'class':'form-select'}),
            'q38b':forms.Select(attrs={'class':'form-select'}),
            'q38c':forms.Select(attrs={'class':'form-select'}),
            'q39a':forms.Select(attrs={'class':'form-select'}),
            'q39b':forms.Select(attrs={'class':'form-select'}),
            'q40a':forms.Select(attrs={'class':'form-select'}),
            'q40b':forms.Select(attrs={'class':'form-select'}),
            'q40c':forms.Select(attrs={'class':'form-select'}),
            'q41':forms.TextInput(attrs={'class':'form-control'}),
            'q42a':forms.Select(attrs={'class':'form-select'}),
            'q42b':forms.Select(attrs={'class':'form-select'}),
            'q43':forms.TextInput(attrs={'class':'form-control'}),
            'q44':forms.Select(attrs={'class':'form-select'}),
            'q45':forms.Select(attrs={'class':'form-select'}),
            'q46':forms.Select(attrs={'class':'form-select'}),
            'q47':forms.Select(attrs={'class':'form-select'}),
            'q48':forms.Select(attrs={'class':'form-select'}),
            'q49':forms.Select(attrs={'class':'form-select'}),
            'q50a':forms.Select(attrs={'class':'form-select'}),
            'q50b':forms.Select(attrs={'class':'form-select'}),
            'q51':forms.Select(attrs={'class':'form-select'}),
            'q52':forms.Select(attrs={'class':'form-select'}),



        }
Inhabitants_InlineForm=inlineformset_factory(Households,Inhabitants,form=InhabitantsForm,extra=1)