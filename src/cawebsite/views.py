from django.views import generic


class CaHomeView(generic.TemplateView):
    template_name = 'cawebsite/caindex.html'

class CaOrganisationView(generic.TemplateView):
    template_name = 'cawebsite/ca_organisation.html'

class ServiceDetailsPage(generic.TemplateView):
    template_name = 'cawebsite/ca_services.html'