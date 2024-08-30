from django.db import transaction
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .serializers import (
    DomainSerializer,
    CreateTenantSerializer
)
from utilities.utils import ResponseInfo


class CreateTenantAPIView(CreateAPIView):
    """
    Class for create tenant api.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = CreateTenantSerializer

    def __init__(self, **kwargs):
        """
        Constructor method for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(CreateTenantAPIView, self).__init__(**kwargs)


    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        """
        POST method for save the tenant and domain data.
        """
        tenant_serializer = self.get_serializer(data=request.data)
        if tenant_serializer.is_valid(raise_exception=True):
            # save the tenant data
            tenant_serializer.save()
            
            # create domain data 
            domain_serializer = DomainSerializer(data={
                "domain": request.data['schema_name'],
                "is_primary": True,
                "tenant": tenant_serializer.data.get("id", None)
            })

            domain_serializer.is_valid(raise_exception=True)
            domain_serializer.save()

            # print("TENANT DATA >>> ", tenant_serializer.data)
            # print("DOMAIN DATA >>> ", domain_object_data)


            self.response_format["data"] = {
                "tenant_data": tenant_serializer.data,
                "domain_data": domain_serializer.data
            }
            self.response_format["message"] = "Nouveau locataire créé avec succès."

            return Response(self.response_format)