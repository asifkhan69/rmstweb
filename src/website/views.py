from django.shortcuts import render
from django.views import generic
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from .forms import ClientQueryForm
from website.genfunctions import send_email_notification

class HomeView(generic.TemplateView):
    template_name = 'website/index.html'


class OrganisationPage(generic.TemplateView):
    template_name = 'website/organisation.html'


class ServiceDetailsPage(generic.TemplateView):
    template_name = 'website/services.html'


class ClientQueryHXView(View):
    def post(self, request, *args, **kwargs):
        form = ClientQueryForm(request.POST)
        if form.is_valid():
            form.save()
            # send email to the info@rmstechknowledgy.com
            status = send_email_notification(settings.SERVER_EMAIL, subject="Client Query Submitted From RMST-Website - PK")
            if status == 202:
                return HttpResponse('<div class="alert alert-success">Your message has been sent successfully. A Company coordinator will contact to the mentioned email address. Thank you! </div>')
        return render(request, 'partials/website/contact_form.html', {'form': form})