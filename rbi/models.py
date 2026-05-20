from django.db import models

class Barangay(models.Model):
    name=models.CharField(max_length=100,null=False,unique=True)
    logo=models.FileField(upload_to="logo/")
    def __str__(self):
        return self.name

class Sitio(models.Model):
    description=models.CharField(max_length=50,null=False)
    barangay=models.ForeignKey(Barangay,on_delete=models.CASCADE,related_name='barangay')

class Sector(models.Model):
    description=models.CharField(max_length=100)

class Relationship(models.Model):
    description=models.CharField(max_length=100)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'

class Sex(models.Model):
    description=models.CharField(max_length=6)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
class Nationality(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'

class MaritalStatus(models.Model):
    description=models.CharField(max_length=250)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class Education(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    

class Ethnicity(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.description}'

class CurrentlyEnrolled(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class HighEducation(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class Religion(models.Model):
    description=models.CharField(max_length=500)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.description}'

class SchoolLevel(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class SourceIncome(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'

class StatusWork(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class PlaceDelivery(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class PersonAssistedDelivery(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class FPMethod(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
class SourceFP(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'

class HealthInsurance(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'

class FacilityVisited(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class ReasonVisit(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class TypeResident(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class ReasonsLeaving(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class ReasonTransferring(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
class Skills(models.Model):
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    def __str__(self):
        return f'{self.code} {self.description}'
    
