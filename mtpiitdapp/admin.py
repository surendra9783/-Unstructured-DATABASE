from django.contrib import admin
from .models import TA_ship,TA_shipnew,MS_Student, PHD_Student,Mtech_Student,Btech_Student
import json
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from prettyjson import PrettyJSONWidget
# from django.contrib.admin import SimpleListFilter
from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from import_export.admin import ImportExportModelAdmin
import uuid
# Register your models here.


# new add demo things

# new demo things end

class TaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    list_display = ('name','ta_entry','courses','details','other_details',)
    search_fields = ('meta_data',)
    # list_display_links = ('name','age','ta_entry','courses')
    # list_filter = ('CompanyFilter')
    # list_filter = [CompanyFilter]
    # search_fields = ('ta_user','ta_entry','ta_course','reco_by')
    list_per_page = 3

    def name(self, instance):
        data = instance.meta_data
        if (data == None):
            return "null"
        try:
            return data["name"]
        except KeyError:
            return "null"
    def age(self, instance):
        data = instance.meta_data
        if (data == None):
            return "null"
        try:
            return data["age"]
        except KeyError:
            return "null"
    def ta_entry(self, instance):
        data = instance.meta_data
        if (data == None):
            return "null"
        try:
            return data["ta_entry"]
        except KeyError:
            return "null"
    def courses(self, instance):
        data = instance.meta_data
        if (data == None):
            return "null"
        try:
            return data["courses"]
        except KeyError:
            return "null"
    def details(self, instance):
        data = instance.meta_data
        if (data == None):
            return "null"
        try:
            return data["details"]
        except KeyError:
            return "null"

    def other_details(self, instance):
        data = instance.meta_data
        if (data == None):
            return "null"
        try:
            return data["other_details"]
        except KeyError:
            return "null"


class TaAdminship(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    # formfield_overrides = {
    #     models.JSONField: {'widget': PrettyJSONWidget}
    # }
    list_display = ('ta_user','ta_course','ta_entry','reco_by')
    search_fields = ('ta_user','ta_course','ta_entry','reco_by')
    list_display_links = ('ta_user','ta_course','ta_entry','reco_by')
    list_filter = ('ta_user','ta_course')
    # search_fields = ('ta_user','ta_entry','ta_course','reco_by')
    list_per_page = 3

# proxy for TA_ship for import-export
class ImportIntoTa_ship(TA_shipnew):
    class Meta:
        proxy = True


# class exampleAdmin(admin.ModelAdmin):
#     list_display = ('ta_user','ta_course','ta_entry','reco_by')
#     list_per_page = 3

# for importexport
class BrandAdmin(ImportExportModelAdmin):
    pass

admin.site.register(TA_ship,TaAdminship)
admin.site.register(ImportIntoTa_ship,BrandAdmin)
admin.site.register(TA_shipnew,TaAdmin)
admin.site.register(MS_Student,TaAdmin)
admin.site.register(PHD_Student,TaAdmin)
admin.site.register(Mtech_Student,TaAdmin)
admin.site.register(Btech_Student,TaAdmin)