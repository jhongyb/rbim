from django.urls import path
from . import views
from . import rbireport


urlpatterns=[
    path('',views.households,name='households'),
    path('newhousehold',views.newhouseholds,name='newhousehold'),
    path('householdlist',views.householdlist,name='householdlist'),
    path('updatehousehold/<pk>',views.household_update,name='household_update'),
    path('deletehousehold/<pk>',views.household_delete,name='household_delete'),


    path('inhabitantslist',views.inhabitantslist,name='inhabitantslist'),
    path('inhabitants@<pk>',views.inhabitant_members,name='inhabitants'),
    path('household/members/<int:pk>/', views.inhabitant_members, name='inhabitant_members'),

    path('rbi/formb/<pk>/',rbireport.rbiformb,name='rbiformb'),
    path('rbi/forma/<pk>/',rbireport.rbiforma,name='rbiforma'),
]