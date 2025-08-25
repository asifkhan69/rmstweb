from django.urls import path
from sgwebsite.views import (SgHomeView)

urlpatterns = [
    # Singapore Home website View
    path('', SgHomeView.as_view(), name='sghome'),

]
