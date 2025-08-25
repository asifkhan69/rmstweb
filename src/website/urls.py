from django.urls import path
from website.views import (HomeView, OrganisationPage, ServiceDetailsPage, ClientQueryHXView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('organisation/', OrganisationPage.as_view(), name='organisation-page'),
    path('services/', ServiceDetailsPage.as_view(), name='services-page'),
    # Client Query
    path('contact/hx-submit/', ClientQueryHXView.as_view(), name='client-query-hx'),
]
