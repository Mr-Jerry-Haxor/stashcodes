from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import InternshipApplication

class InternshipApplicationResource(resources.ModelResource):
    class Meta:
        model = InternshipApplication

class InternshipApplicationAdmin(ImportExportModelAdmin):
    resource_class = InternshipApplicationResource
    list_display = ('email', 'name', 'gender', 'domain', 'college', 'contact', 'whatsapp', 'qualification', 'year', 'source')
    search_fields = ('email', 'name', 'college', 'domain')
    list_filter = ('gender', 'year', 'college')

admin.site.register(InternshipApplication, InternshipApplicationAdmin)
admin.site.site_header = 'StashCodes Admin'