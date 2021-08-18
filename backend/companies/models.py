from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'
    
    def __repr__(self):
        return f"<{str(self)}>"


class CompanyPermission(models.Model):
    name = models.CharField(
        _('codename'), max_length=100, help_text='Permission under a given company'
    )
    desc = models.TextField()

    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE,
        related_name='permissions'
    )

    class Meta:
        unique_together = (
            ('company', 'name')
        )

    def __str__(self):
        return f"{self.__class__.__name__}: {self.company.name}'s {self.name} Permission"
    
    def __repr__(self):
        return f"<{str(self)}>"


class CompanyGroup(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    permissions = models.ManyToManyField(
        CompanyPermission,
        verbose_name=_('permissions'),
        blank=True,
    )
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='groups')

    class Meta:
        unique_together = (
            ('company', 'name')
        )

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'
    
    def __repr__(self):
        return f'<{str(self)}>'


class CompanyRole(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    desc = models.TextField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    permissions = models.ManyToManyField(CompanyPermission)

    class Meta:
        unique_together = (
            ('company', 'name')
        )

    def __str__(self):
        return f"{self.__class__.__name__}: {self.company.name}'s {self.name} Role"

    __repr__ = __str__
