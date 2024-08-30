## Build Multitenant SaaS Application using Django and Django Rest Framework

from tenants.models import TenantModel, DomainModel
import os, django

### Setup the public tenant

> - Access to the shell

```{python}
python manage.py shell
```

> - Create the public tenant

```{python}
from 

tenant = TenantModel(schema_name='public', company_name='Schemas Inc.')
tenant.save()
```

> - Create the main domain for public tenant

```{python}
domain = DomainModel()
domain.domain = 'localhost' # don't add your port or www here! on a local server you'll want to use localhost here
domain.tenant = tenant
domain.is_primary = True
domain.save()
```

# create your first real tenant

tenant = TenantModel(schema_name='jupitergroup',
name='Jupiter Hospital',
paid_until='2024-12-05',
on_trial=True)
tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

# # Add one or more domains for the tenant

domain = DomainModel()
domain.domain = 'jupiter' # don't add your port or www here!
domain.tenant = tenant
domain.is_primary = True
domain.save()
