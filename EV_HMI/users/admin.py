from django.contrib import admin
from .models import Profile, Company, CompanyEmployee


admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(CompanyEmployee)
