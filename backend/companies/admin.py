from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
    Company, CompanyGroup, CompanyRole, CompanyPermission
)

admin.site.unregister(Group)

admin.site.register(Company)
admin.site.register(CompanyGroup)
admin.site.register(CompanyRole)
admin.site.register(CompanyPermission)
