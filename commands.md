from tenants.models import Tenant, Domain
from users.models import CustomUser


tenant1 = Tenant()
tenant1.schema_name = "public"
tenant1.company_name = "Defaut Inc."
# tenant1.ip_address = "192.168.1.12"
tenant1.is_active = True
tenant1.save()

domain1 = Domain()
domain1.domain = "localhost"
domain1.is_primary = True
domain1.tenant = tenant1
domain1.save()

tenant2 = Tenant()
tenant2.schema_name = "hp"
tenant2.company_name = "Health Performance"
# tenant2.ip_address = "192.168.1.12"
tenant2.is_active = True
tenant2.save()

domain2 = Domain()
domain2.domain = tenant2.schema_name
domain2.is_primary = True
domain2.tenant = tenant2
domain2.save()
