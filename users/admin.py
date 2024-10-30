from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import InternshipApplication, Contact, webhook_logs

class InternshipApplicationResource(resources.ModelResource):
    class Meta:
        model = InternshipApplication

class InternshipApplicationAdmin(ImportExportModelAdmin):
    resource_class = InternshipApplicationResource
    list_display = ('email', 'name', 'gender', 'domain', 'college', 'contact', 'whatsapp', 'qualification', 'year', 'source')
    search_fields = ('email', 'name', 'college', 'domain')
    list_filter = ('gender', 'year', 'college')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')

class WebhookLogsAdmin(admin.ModelAdmin):
    list_display = ('log', 'log_time')
    search_fields = ('log',)

admin.site.register(InternshipApplication, InternshipApplicationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(webhook_logs, WebhookLogsAdmin)

admin.site.site_header = 'StashCodes Admin'