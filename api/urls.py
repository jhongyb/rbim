from django.urls import path
from .views import Secure_Inhabitants,Secure_Household


urlpatterns=[
    path('api/rbim',Secure_Inhabitants.as_view(),name='rbimapi'),
    path('api/rbim/household',Secure_Household.as_view(),name='rbihousehold'),
    ]