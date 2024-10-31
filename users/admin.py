from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import InternshipApplication, Contact, webhook_logs

class InternshipApplicationResource(resources.ModelResource):
    class Meta:
        model = InternshipApplication

class InternshipApplicationAdmin(ImportExportModelAdmin):
    resource_class = InternshipApplicationResource
    list_display = ('email', 'name', 'gender', 'domain', 'college', 'contact', 'address', 'qualification', 'year', 'ispaid', 'time')
    search_fields = ('email', 'name', 'college', 'domain')
    list_filter = ('gender', 'year', 'college', 'domain', 'ispaid', 'time')

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'message' , 'time')
    search_fields = ('name', 'email')
    list_filter = ('time',)

class WebhookLogsAdmin(ImportExportModelAdmin):
    list_display = ('log', 'log_time')
    

admin.site.register(InternshipApplication, InternshipApplicationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(webhook_logs, WebhookLogsAdmin)

admin.site.site_header = 'StashCodes Admin'