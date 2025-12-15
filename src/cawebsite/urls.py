from django.urls import path
from cawebsite.views import (CaHomeView, CaOrganisationView, ServiceDetailsPage)

urlpatterns = [
    # Canada Home website View
    path('', CaHomeView.as_view(), name='cahome'),
    path('organisation/', CaOrganisationView.as_view(), name='caorganisation-page'),
    path('services/', ServiceDetailsPage.as_view(), name='caservices-page'),

]