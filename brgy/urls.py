from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns=[
    path('Barangay/',views.RBIbarangay, name='rbibarangay'),
    path('Barangay/formc<b>',views.RBIformc, name='rbiformc')
]

# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
