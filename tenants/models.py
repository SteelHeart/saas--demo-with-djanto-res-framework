from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    company_name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    siret_number = models.CharField(max_length=255, null=True, blank=True)
    activity_area = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    company_size = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    auto_create_schema = True

    class Meta:
        db_table = 'tenants'
        ordering = ['created_at']


class Domain(DomainMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null= True, blank= True)
    deleted_at = models.DateTimeField(null= True, blank= True)
    auto_create_schema = True

    class Meta:
        db_table = 'domains'
        ordering = ['created_at']
        verbose_name = 'Domain'
        verbose_name_plural = 'Domains'