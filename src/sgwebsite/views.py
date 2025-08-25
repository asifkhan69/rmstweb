from django.shortcuts import render
from django.views import generic


class SgHomeView(generic.TemplateView):
    template_name = 'sgwebsite/sgindex.html'
