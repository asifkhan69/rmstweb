"""
General Functions. genfunctions.py
"""

from django.conf import settings
from django.template.loader import render_to_string
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

"""
send_email_notification is used to send emails notification via Sendgrid API
"""
def send_email_notification(emailto, **kwargs):
    context = {}
    emailsubject = kwargs.get('subject', '')
    emailbody = kwargs.get('body', '')
    context['emailto'] = emailto
    context['emailsubject'] = emailsubject
    context['emailbody'] = emailbody

    html_message = render_to_string('partials/website/email_notification.html', context)
    message = Mail(
        from_email= settings.DEFAULT_FROM_EMAIL,
        to_emails= emailto,
        subject= emailsubject,
        html_content= html_message)
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        return e.message

    return response.status_code