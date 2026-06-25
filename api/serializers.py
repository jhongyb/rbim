from django.test import TestCase

# Create your tests here.
from rest_framework import serializers
from inhabitants.models import Inhabitants,Households
from rbi.models import Barangay

class Inhabitants_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Inhabitants
        fields='__all__'

class Household_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Households
        fields='__all__'


class Barangay_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Barangay
        fields='__all__'

