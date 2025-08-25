from django.contrib import admin

from .models import ClientQuery

class ClientQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status')
    list_filter = ('status',)
    search_fields = ('name','email')

    class Meta:
        model = ClientQuery




''' Customize Admin site values '''
admin.site.site_header = 'RMS Techknowledgy Site Administration'
admin.site.site_title = 'RMS Techknowledgy App Administration'
admin.site.index_title = 'RMS Techknowledgy Site Administration'

''' Register the model for admin '''
admin.site.register(ClientQuery, ClientQueryAdmin)
