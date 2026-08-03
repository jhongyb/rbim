from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from . import chartviews


urlpatterns=[
    path('Barangay/',views.RBIbarangay, name='rbibarangay'),
    path('Barangay/formc<b>',views.RBIformc, name='rbiformc'),
    path('Barangay/Indicators',views.rbimindicators, name='rbimindicators'),

    path('Barangay/Indicators/popbysex/<pk>',chartviews.population_by_sex, name='populationbysex'),
    path('Barangay/Indicators/popbycivilstatus/<pk>',chartviews.population_by_civilstatus, name='populationbycivilstatus'),
    path('Barangay/Indicators/popbyreligion/<pk>',chartviews.population_by_religion, name='populationbyreligion'),
    path('Barangay/Indicators/popbyethnicity/<pk>',chartviews.population_by_ethnicity, name='populationbyethnicity'),
    path('Barangay/Indicators/popbynationality/<pk>',chartviews.population_by_nationality, name='populationbynationality'),
    path('Barangay/Indicators/popbyhigheducation/<pk>',chartviews.population_by_higheducation, name='populationbyhigheducation'),

    ]
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
