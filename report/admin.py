from django.contrib import admin

# Register your models here.
from report.models import CrimeType, City, State, AddressType, Report

admin.site.register(CrimeType)
admin.site.register(City)
admin.site.register(State)
admin.site.register(AddressType)
admin.site.register(Report)

