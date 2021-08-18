from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from companies.models import Company, CompanyPermission
from uam_prj.validators import mobile_validator


class EmployeeManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields['company'] = Company.objects.get_or_create(name='admin')[0]
        super().create_superuser(username, email, password, **extra_fields)


class Employee(AbstractUser):
    REQUIRED_FIELDS = ['email', 'mobile_no']

    objects = EmployeeManager()

    mobile_no = models.CharField(
        max_length=20, unique=True, validators=[mobile_validator]
    )

    company = models.ForeignKey('companies.Company', on_delete=models.DO_NOTHING)

    role = models.ForeignKey(
        'companies.CompanyRole', on_delete=models.DO_NOTHING,
        null=True, blank=True
    )
    groups = models.ManyToManyField('companies.CompanyGroup')

    def has_company_perm(self, perm_name):
        return perm_name in CompanyPermission.objects.filter(
            models.Q(companygroup__employee=self) 
            | models.Q(companyrole__employee=self)
        ).values_list('name', flat=True)
