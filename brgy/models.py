from django.db import models
from django.contrib.auth.models import User
from rbi.models import Barangay

class UserBarangay(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    brgy=models.ForeignKey(Barangay,on_delete=models.CASCADE)
    dateadded=models.DateField(auto_now_add=True)


