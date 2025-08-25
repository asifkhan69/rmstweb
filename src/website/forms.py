import logging
from django import forms
from .models import ClientQuery

logger = logging.getLogger(__name__)  # Use module-level logger

class ClientQueryForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ClientQuery
        fields = ['name', 'email', 'message']

    def clean_website(self):
        data = self.cleaned_data.get('website')
        if data:
            # Log bot attempt with available request data if possible
            logger.warning(f"Bot detected via honeypot: data={data}")
            raise forms.ValidationError("Bot detected.")
        return data