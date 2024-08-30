from rest_framework import serializers
from .models import (Tenant, Domain)


class CreateTenantSerializer(serializers.ModelSerializer):
    """
    Class for create tenant serializer.
    """
    # domain = serializers.CharField(required=True, write_only=True)
    # domain_name = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Tenant
        fields = ("id", "schema_name", "company_name", "logo", "siret_number", "activity_area", "website_url", "company_size", "is_active", "created_at", "updated_at", "deleted_at",)



class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = ("id", "domain", "tenant", "is_primary")
