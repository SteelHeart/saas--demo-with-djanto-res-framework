from django.urls import path

from .views import CreateTenantAPIView


urlpatterns = [
    path("create-tenant", CreateTenantAPIView.as_view(), name="create-tenant")
]
