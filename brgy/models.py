from django.db import models
from django.contrib.auth.models import User
from rbi.models import Barangay

class UserBarangay(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    brgy=models.ForeignKey(Barangay,on_delete=models.CASCADE)
    dateadded=models.DateField(auto_now_add=True)


class PageAccess(models.Model):
    pageuser=models.ForeignKey(User,on_delete=models.CASCADE)
    page=models.CharField(max_length=100,choices=[('ADMIN_PAGE','admin_page'),('OTHERS','others')])
    dateadded=models.DateField(auto_now_add=True)



