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
    path('Barangay/Indicators/popbycivilstatus/<pk>',chartviews.population_by_civilstatus, name='populationbycivilstatus')
]
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
