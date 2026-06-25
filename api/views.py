from django.shortcuts import render

import requests
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Count,Q

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from inhabitants.models import Inhabitants,Households
from .serializers import Inhabitants_Serializer,Household_Serializer
from rest_framework.response import Response



class Secure_Inhabitants(ListAPIView):
    # OPTIMIZED: Added select_related to fetch joined data in a single query
    queryset = Inhabitants.objects.select_related('hh', 'hh__barangay').all()
    serializer_class = Inhabitants_Serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [SearchFilter]
    search_fields = ['lastname', 'firstname']


class Secure_Household(ListAPIView):
    # OPTIMIZED: Added select_related to fetch joined data in a single query
    queryset = Households
    serializer_class = Household_Serializer

